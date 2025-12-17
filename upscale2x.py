#!/usr/bin/env python3
"""
upscale2x.py (v2)
=================
고품질 AI 업스케일러 (2배 기본)
- OpenCV dnn_superres 사용 (EDSR, FSRCNN, LapSRN 등)
- RGBA(투명 PNG) 자동 지원
- Pillow Lanczos 폴백

사용법:
    python upscale2x.py input.png output.png
    python upscale2x.py -m ./EDSR_x2.pb input.jpg output.png
"""

import argparse
import os
import sys

def try_import_cv2():
    try:
        import cv2
        return cv2
    except Exception:
        return None


def upscale_with_dnn_superres(cv2, img_path, out_path, model_path=None, scale=2, model_name_hint=None):
    """
    OpenCV dnn_superres를 사용하여 업스케일.
    RGBA 입력도 자동 처리 (Alpha 분리 후 병합).
    """
    from cv2 import dnn_superres
    from PIL import Image
    import numpy as np

    sr = dnn_superres.DnnSuperResImpl_create()

    # 모델 로드
    if model_path:
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        sr.readModel(model_path)
    elif model_name_hint:
        guess = os.path.join(os.getcwd(), model_name_hint)
        if os.path.exists(guess):
            sr.readModel(guess)
        else:
            raise FileNotFoundError(f"No model found at {guess}. Please provide a model file (EDSR_x2, FSRCNN_x2, ...)")
    else:
        raise ValueError("No model_path or model_name_hint provided for dnn_superres.")

    # 모델 이름 추정
    model_type = "edsr" if "EDSR" in (model_path or model_name_hint).upper() else \
                 "fsrcnn" if "FSRCNN" in (model_path or model_name_hint).upper() else \
                 "lapsrn"
    sr.setModel(model_type, scale)

    # 이미지 읽기
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Cannot read input image: {img_path}")

    # RGBA 입력 처리
    if img.ndim == 3 and img.shape[2] == 4:
        # BGRA → BGR + A 분리
        bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        alpha = img[:, :, 3]

        # RGB 업스케일
        up_rgb = sr.upsample(bgr)

        # Alpha 업스케일 (Lanczos)
        from PIL import Image
        alpha_img = Image.fromarray(alpha)
        w, h = alpha_img.size
        alpha_up = alpha_img.resize((w * scale, h * scale), Image.LANCZOS)
        alpha_up = np.array(alpha_up)

        # RGB + Alpha 합성
        up_rgba = cv2.cvtColor(up_rgb, cv2.COLOR_BGR2BGRA)
        up_rgba[:, :, 3] = alpha_up

        cv2.imwrite(out_path, up_rgba)
        return out_path

    else:
        # 일반 RGB or Grayscale
        result = sr.upsample(img)
        cv2.imwrite(out_path, result)
        return out_path


def upscale_with_pillow(img_path, out_path, scale=2):
    """Pillow로 Lanczos 업스케일 (RGBA 포함)"""
    from PIL import Image
    im = Image.open(img_path)
    w, h = im.size
    new_size = (w * scale, h * scale)
    up = im.resize(new_size, Image.LANCZOS)
    up.save(out_path)
    return out_path


def main():
    p = argparse.ArgumentParser(description="AI 2x Upscaler (OpenCV dnn_superres + RGBA 지원)")
    p.add_argument("input", help="입력 이미지 경로")
    p.add_argument("output", help="출력 이미지 경로")
    p.add_argument("-r", "--scale", type=int, default=2, help="확대 배율 (기본 2)")
    p.add_argument("-m", "--model", default=None, help="dnn_superres 모델 파일 경로 (예: EDSR_x2.pb)")
    p.add_argument("--model-name", default=None, help="모델 이름 힌트 (예: EDSR_x2.pb)")
    args = p.parse_args()

    input_path = args.input
    output_path = args.output
    scale = args.scale

    if not os.path.exists(input_path):
        print("입력 이미지가 존재하지 않습니다:", input_path, file=sys.stderr)
        sys.exit(2)

    cv2 = try_import_cv2()
    tried_dnn = False
    if cv2:
        try:
            if hasattr(cv2, "dnn_superres") or hasattr(cv2, "dnn"):
                tried_dnn = True
                try:
                    model_path = args.model
                    model_hint = args.model_name
                    if model_path is None and model_hint is None:
                        model_hint = "EDSR_x2.pb"
                    upscale_with_dnn_superres(cv2, input_path, output_path, model_path=model_path, scale=scale, model_name_hint=model_hint)
                    print("✅ 업스케일 완료 (OpenCV dnn_superres) →", output_path)
                    return
                except Exception as e:
                    print("⚠️ OpenCV dnn_superres 실패:", e, file=sys.stderr)
                    print("Pillow Lanczos로 폴백합니다...", file=sys.stderr)
        except Exception as e:
            print("dnn_superres 사용 불가:", e, file=sys.stderr)

    # Pillow 폴백
    try:
        from PIL import Image
    except Exception:
        print("Pillow 미설치. 설치: pip install pillow", file=sys.stderr)
        sys.exit(3)

    upscale_with_pillow(input_path, output_path, scale=scale)
    print("✅ 업스케일 완료 (Pillow Lanczos) →", output_path)


if __name__ == "__main__":
    main()