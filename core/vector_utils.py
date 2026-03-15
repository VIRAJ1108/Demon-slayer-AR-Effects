import numpy as np


def extend_vector(start, end, length=200):

    start = np.array(start)
    end = np.array(end)

    direction = end - start

    norm = np.linalg.norm(direction)

    if norm == 0:
        return tuple(end)

    direction = direction / norm

    new_point = end + direction * length

    return tuple(new_point.astype(int))