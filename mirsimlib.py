import numpy as np


def hypot(vec):
    return np.sqrt(np.sum(vec**2, axis=1))
