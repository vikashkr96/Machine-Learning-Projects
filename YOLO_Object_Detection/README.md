# Flask YOLO Object Detection

A real-time object detection system built using **YOLOv3**, **OpenCV**, and **Flask**.  
This project opens the webcam and detects objects in real time using a pretrained YOLOv3 model.

---

## 🎥 Demo

![YOLO Object Detection Demo](demo.gif)

▶ **Watch Full Video:** [https://youtube.com/YOUR_VIDEO_LINK](https://youtu.be/7CdXu27JjUU?si=C6O4ffyBLFuzVkcL)

---

## Features

- Real-time object detection
- Webcam streaming
- YOLOv3 deep learning model
- Flask web interface
- Simple UI

---

## Tech Stack

- Python
- Flask
- OpenCV
- YOLOv3
- HTML / CSS

---

## Project Structure

flask_object_detection/

│

├── app.py

├── model.py

├── requirements.txt

├── yolov3.cfg

├── yolov3.weights

├── coco.names

├── .gitignore

├── README.md

│

└── templates/

&nbsp;&nbsp;&nbsp;&nbsp;└── index.html

---

## Setup and Run (Step by Step)

### 1. Clone the repository

git clone https://github.com/vikashkr96/Machine-Learning-Projects.git

**Note:**

Download YOLO weights from:

https://pjreddie.com/media/files/yolov3.weights

Download YOLO configuration file from:

https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg

Download COCO Dataset file from:

https://github.com/pjreddie/darknet/blob/master/data/coco.names

Place all the three files inside this project folder.

---

### 2. Create Virtual Environment

python -m venv venv

---

### 3. Activate Virtual Environment

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

---

### 4. Install Requirements

pip install -r requirements.txt

---


### 5. Run the Project

python app.py

---

### 6. Open Browser

http://127.0.0.1:5000

Click **Run Model and Open Camera**.

The webcam will start and objects will be detected in real time.

---

## Objects Detected

YOLOv3 is trained on the **COCO dataset** and detects **80 classes**, such as:

- 👤 Person

- 🚗 Car

- 🚲 Bicycle

- 🐶 Dog

- 🐱 Cat

- 🍾 Bottle

- 💻 Laptop

- 📱 Mobile Phone

- 🎒 Backpack

- 🚦 Traffic Light

- 🪑 Chair

and many more .....

---

## Requirements

Flask

opencv-python

numpy

Install using:

pip install -r requirements.txt

---


## Author

Vikash Kumar

---

## License

This project is open source and free to use for educational purposes.
