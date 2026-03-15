import cv2

def draw_particles(frame, particles):

    for p in particles:

        cv2.circle(
            frame,
            (int(p.x), int(p.y)),
            4,
            (255,200,0),
            -1
        )