import cv2
import numpy as np


class EffectRenderer:

    def __init__(self, image_path):

        self.effect = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)


    def render(self, frame, start, end):

        x1, y1 = start
        x2, y2 = end

        length = int(np.hypot(x2-x1, y2-y1))
        angle = np.degrees(np.arctan2(y2-y1, x2-x1))

        effect = cv2.resize(self.effect, (length, 200))

        h, w = effect.shape[:2]

        center = (w//2, h//2)

        rot_matrix = cv2.getRotationMatrix2D(center, angle, 1)

        rotated = cv2.warpAffine(
            effect,
            rot_matrix,
            (w, h),
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_TRANSPARENT
        )

        x = int(x1 - w/2)
        y = int(y1 - h/2)

        self.alpha_blend(frame, rotated, x, y)

        return frame


    def alpha_blend(self, frame, overlay, x, y):

        h, w = overlay.shape[:2]

        if x < 0 or y < 0:
            return

        if x+w > frame.shape[1] or y+h > frame.shape[0]:
            return

        alpha = overlay[:,:,3] / 255.0

        for c in range(3):

            frame[y:y+h, x:x+w, c] = (
                alpha * overlay[:,:,c] +
                (1-alpha) * frame[y:y+h, x:x+w, c]
            )