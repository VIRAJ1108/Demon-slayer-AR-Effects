import mediapipe as mp
import cv2

class PoseDetector:

    def __init__(self):

        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.pose.process(rgb)

        return results

    def draw_pose(self, frame, results):

        if results.pose_landmarks:
            self.mp_draw.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

        return frame
    
    def get_arm_points(self, frame, results):

        if not results.pose_landmarks:
            return None

        h, w, _ = frame.shape
        landmarks = results.pose_landmarks.landmark

        elbow = landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        wrist = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value]

        elbow_point = (int(elbow.x * w), int(elbow.y * h))
        wrist_point = (int(wrist.x * w), int(wrist.y * h))

        return elbow_point, wrist_point