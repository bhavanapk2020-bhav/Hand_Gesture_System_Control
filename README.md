# Gesture-Based System Control

This project enables real-time hand gesture recognition using a webcam to control system functions. By leveraging MediaPipe for hand tracking and OpenCV for image processing, finger-count gestures are mapped to actions such as brightness adjustment, taking screenshots, and opening Task View.

## Features
 Real-time hand tracking with MediaPipe
 Finger-count based gesture recognition
 System actions:
  - 1 finger → Increase brightness (+10)
  - 2 fingers → Take screenshot (Win + PrtSc)
  - 3 fingers → Open Task View (Win + Tab)
- Visual feedback with hand landmarks and finger count displayed on the video feed
- Actions trigger only when the gesture changes

## Tech Stack
- MediaPipe – Hand tracking and landmark detection
- OpenCV    – Webcam capture and image processing
- PyAutoGUI – Automating system-level keyboard shortcuts
- Screen Brightness Control – Adjusting display brightness
