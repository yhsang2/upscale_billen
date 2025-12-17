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

## 📂 Project Structure
upscale_billen/
├── input.jpg # Original image
├── output.jpg # Upscaled image (generated)
├── upscale.py # Main script
└── README.md

📌 Description

input.jpg
The original image you want to upscale.

output.jpg
The generated image with doubled resolution.

upscale.py
The core script that performs the image upscaling.

requirements.txt
Lists all required Python libraries.

README.md
Project documentation and usage guide.


---

## 🚀 How It Works

1. Loads `input.jpg`
2. Applies an image upscaling algorithm
3. Outputs a **2× higher-resolution image** as `output.jpg`

---

## 🛠️ Requirements

- Python 3.8+
- Required Python libraries:
  ```bash
  pip install pillow opencv-python
  (Exact libraries may vary depending on implementation.)
  ```
