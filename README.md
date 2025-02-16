# Face Recognition-Based Attendance System

## Description

This project automates attendance tracking using face recognition. It captures classroom images, detects and recognizes student faces, and marks attendance in a spreadsheet, which is then uploaded to a web platform. Additionally, the system includes an automated image-capturing mechanism using a linear actuator and a timer to take images at the beginning of each class hour.

## Features

- **Student Dataset Collection**: Stores student images along with their names and roll numbers.
- **Face Recognition Model**: Trained to identify students based on the dataset.
- **Automated Image Capturing**: Uses a linear actuator and timer to capture class images at scheduled times.
- **Face Detection & Cropping**: Extracts individual faces from the captured class image.
- **Attendance Marking**: Matches detected faces with the dataset and logs attendance in a spreadsheet.
- **Automated Spreadsheet Upload**: Attendance data is uploaded to a designed website for easy access.

## Installation & Setup

### 1. Prerequisites

Ensure you have **Python** installed along with necessary dependencies:

```sh
pip install opencv-python numpy pandas face-recognition
```

### 2. Usage

1. **Dataset Preparation**  
   - Collect student images and store them with names and roll numbers.  
   - Train the face recognition model using the dataset.  

2. **Running the System**  
   - The system captures an image of the classroom at the beginning of each class hour.  
   - Faces are detected, cropped, and compared with the dataset.  
   - If a match is found, attendance is marked in a spreadsheet.  
   - The updated spreadsheet is automatically uploaded to the web platform.  

3. **Automated Image Capture**  
   - The system is integrated with a linear actuator and timer for hands-free operation.

## Future Enhancements

- **Live video-based attendance tracking**  
- **Cloud storage integration for attendance records**  
- **Mobile app for real-time monitoring**  

## Author  
**Nandhini K**
