import cv2
import numpy as np

from core.camera import Camera
from core.pose_detector import PoseDetector
from core.vector_utils import extend_vector
from effects.effect_renderer import EffectRenderer


def main():

    cam = Camera()
    pose_detector = PoseDetector()

    # Load slash effect
    water_effect = EffectRenderer("assets/png-transparent-flowing-water-blue-water-splashing-removebg-preview.png")
    flame_effect = EffectRenderer("assets/fire_slash-removebg-preview.png")

    current_effect = "water"

    water_trail = 8
    flame_trail = 3

    water_duration = 8
    flame_duration = 4

    # Motion detection variables
    prev_wrist = None
    swing_threshold = 35
    show_effect_frames = 0
    wrist_history = []
    history_size = 5
    attack_cooldown = 0
    trail_history = []
    trail_length = 8

    while True:

        frame = cam.get_frame()

        if frame is None:
            break

        # Pose detection
        results = pose_detector.detect(frame)

        frame = pose_detector.draw_pose(frame, results)

        arm_points = pose_detector.get_arm_points(frame, results)

        if arm_points:

            elbow, wrist = arm_points

            # Extend sword direction
            sword_tip = extend_vector(elbow, wrist, length=300)

            # Debug visualization
            cv2.circle(frame, elbow, 8, (0,255,0), -1)
            cv2.circle(frame, wrist, 8, (0,0,255), -1)

            cv2.line(frame, elbow, wrist, (255,0,0), 4)
            cv2.line(frame, wrist, sword_tip, (255,0,0), 4)

            # --- store wrist history ---
            wrist_history.append(wrist)

            if len(wrist_history) > history_size:
                wrist_history.pop(0)

            # --- compute smoothed position ---
            avg_x = int(np.mean([p[0] for p in wrist_history]))
            avg_y = int(np.mean([p[1] for p in wrist_history]))

            smoothed_wrist = (avg_x, avg_y)

            # ---- motion detection ----
            if prev_wrist is not None and attack_cooldown == 0:

                dx = smoothed_wrist[0] - prev_wrist[0]
                dy = smoothed_wrist[1] - prev_wrist[1]

                speed = np.sqrt(dx*dx + dy*dy)

                if speed > swing_threshold:
                    if current_effect == "water":
                        show_effect_frames = water_duration
                    else:
                        show_effect_frames = flame_duration
                    attack_cooldown = 10

            prev_wrist = smoothed_wrist

            # --- Render slash if swing detected ---
            if show_effect_frames > 0:

                trail_history.append((wrist, sword_tip))

                max_trail = water_trail if current_effect == "water" else flame_trail

                if len(trail_history) > max_trail:
                    trail_history.pop(0)
                show_effect_frames -= 1

           # ---- draw trail ----
        for i, (start, end) in enumerate(trail_history):

            opacity = (i + 1) / len(trail_history)

            if current_effect == "water":
                frame = water_effect.render(frame, start, end, opacity)

            elif current_effect == "flame":
                frame = flame_effect.render(frame, start, end, opacity)


        if attack_cooldown > 0:
            attack_cooldown -= 1

        cv2.putText(frame,
                f"Breathing: {current_effect}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,255,255),
                2
            )


        cv2.imshow("Demon Slayer AR", frame)

        
        key = cv2.waitKey(1) & 0xFF

        if key == ord('1'):
            current_effect = "water"

        if key == ord('2'):
            current_effect = "flame"

        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()