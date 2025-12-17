# 🖼️ Image Upscale Billen

A simple Python project that **upscales an image to 2× resolution**  
while preserving as much visual quality as possible.

This project takes an `input.jpg` file and generates a higher-resolution
image using an image upscaling algorithm.

---

## ✨ Features

- 🔍 Upscales images by **2× resolution**
- 🐍 Simple and clean **Python implementation**
- 📸 Works with standard image formats (JPG, PNG)
- ⚡ Easy to run — minimal setup
- 🎯 Ideal for beginners learning image processing

---

## 🚀 How It Works

1. Loads `input.jpg`
2. Applies an image upscaling algorithm
3. Outputs a **2× higher-resolution image** as `output.jpg`

### 1️⃣ Usage

This program upscales an image to **2× resolution** using a pre-trained model.

### 2️⃣ Prepare the input image

Place the image you want to upscale in the project folder  
(e.g. `input.jpg`).

### 3️⃣ Run the upscaling command

Execute the following command:

```bash
python upscale2x.py -m ./EDSR_x2.pb input.jpg output.png
```

---

## 📂 Project Structure

upscale_billen/
- ├── input.jpg # Original image
- ├── output.jpg # Upscaled image (generated)
- ├── upscale.py # Main script
- └── README.md

---

## 🛠️ Requirements

- Python 3.8+
- Required Python libraries:
  ```bash
  pip install pillow opencv-python
  (Exact libraries may vary depending on implementation.)
  ```
  
---

## 👉 Core Logic

- This code is the **core logic of this project**.
<img width="2285" height="1307" alt="image" src="https://github.com/user-attachments/assets/fd51286f-0076-4e9b-bec8-11c3a99cce1b" />

---

## ☕ Support

If this project helped you,  
you can **buy me a coffee** and support my work :)

👉 **https://buymeacoffee.com/yhsang2**

Thank you! 🙌

---

## 📄 License

This project is licensed under the **MIT License**. @yhsang2
