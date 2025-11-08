# Background Removal using MediaPipe + OpenCV 🎥✨

A real-time **background removal** project using **MediaPipe Selfie Segmentation**  
and **OpenCV**, with support for:

✅ Background Color Replacement  
✅ Background Image Replacement  
✅ Smooth Masking (No Shaking / No Artifacts)  
✅ Real-time Performance  
✅ Works with any webcam

---

## 🚀 Features

### ✅ 1. Background Color Replacement  
Replace your background with any solid color (green, blue, white, etc.).

### ✅ 2. Background Image Replacement  
Automatically cut out the person and place them in front of:
- Office background  
- Nature background  
- Blur effect  
- Any custom image  

### ✅ 3. Smooth Segmentation  
To avoid shaky edges or flickering, the mask is stabilized using:
- Gaussian smoothing  
- Soft blending  
- Frame-to-frame smoothing  

### ✅ 4. Works in Real-Time  
Optimized for performance even on older laptops.

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV**
- **MediaPipe Selfie Segmentation**
- **NumPy**

---

## 📦 Installation

### 1️⃣ Install required libraries

pip install opencv-python mediapipe numpy


### 2️⃣ Clone the repository



git clone https://github.com/mdsanapala/Background-Removal-Project.git

cd Background-Removal-Project


### 3️⃣ Add your background image
Place your custom background image inside the project folder:



background.jpg


---

## ▶️ Run the Project



python background_removal.py


---

## 🎮 How to Use

| Action | Description |
|-------|-------------|
| **1** | Starts webcam feed |
| **C** | Switch to Color Background Mode |
| **I** | Switch to Image Background Mode |
| **Q** | Quit program |

---

## 📂 Project Structure



Background-Removal-Project/
│── background_removal.py
│── background.jpg
│── README.md


---

## 💡 Future Improvements

- Add blurring background (portrait mode)
- Add person outline glow effect
- Add background video support
- Add virtual greenscreen mode

---

## 👤 Author

**mdsanapala**

---

## ⭐ If you liked this project, don't forget to give the repo a star! 🌟
