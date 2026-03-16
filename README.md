Demon Slayer AR Effects

! Demo (assets/water_gif.gif) (assets/flame_gif.gif)

A real-time Augmented Reality sword effect system inspired by the anime Demon Slayer.
The project uses computer vision and pose estimation to track arm motion from a webcam and render anime-style sword slashes when the user performs a swing gesture.

This was built as a fun hobby prototype exploring pose detection, motion detection, and real-time visual effects using Python.

Features

Real-time pose detection using MediaPipe

Sword direction estimation from arm joints (elbow → wrist)

Motion-based attack detection triggered by fast arm swings

Trail rendering system to create slash effects

Fade-out effect trails for smoother visuals

Multiple breathing styles:

Water Breathing

Flame Breathing

Demo Concept

When the user swings their arm in front of the webcam, the system detects the motion and generates an anime-style sword slash effect that follows the direction of the swing.

Arm swing → Motion detection → Slash effect → Trail fade

Controls:

1 → Water Breathing
2 → Flame Breathing
ESC → Exit

**Tech Stack**
Python
OpenCV
MediaPipe
NumPy

MediaPipe is used for real-time pose estimation, while OpenCV handles rendering and webcam interaction.


**How It Works ?**

The webcam captures frames in real time.
MediaPipe detects body pose landmarks.
The system tracks the elbow and wrist to estimate the sword direction.
Fast arm motion is detected using wrist velocity.

When a swing is detected:

A slash effect is rendered along the sword vector
A short trail history creates the flowing effect
Trail opacity gradually fades to create smoother visuals.


**Installation**

Clone the repository:

git clone https://github.com/VIRAJ1108/Demon-slayer-AR-Effects.git
cd Demon-slayer-AR-Effects

Create a virtual environment:

python -m venv venv
venv\Scripts\activate

**Install dependencies:**

pip install -r requirements.txt

**Run the project:**

python main.py
