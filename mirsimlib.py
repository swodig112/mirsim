import numpy as np


def hypot(vec):
    return np.sqrt(np.sum(vec**2, axis=1))


def incross(vec1, vec2):
    return np.sum(vec1 * vec2)
