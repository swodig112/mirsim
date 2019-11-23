import numpy as np


def hypot(vec):
    return np.sqrt(np.sum(vec**2, axis=1))


def incross(vec1, vec2):
    return np.sum(vec1 * vec2)


def sizeondir(vec1, vec2):
    return incross(vec, vec2) / hypot(vec2) ** 2 * vec2


def reflect(vec, point):
    ver = sizeondir(vec, point) + point
    ref = 2 * ver - (point + vec * -1)
    return ref


def shaperesolver(shape):
    res = []
    for i in range(len(shape) - 1):
        res.appen(shape[i] - 1)
    return tuple(res)


def spoint2point(spoint):
    return np.array([np.sin(spoint[0]) * spoint[1],
                     np.cos(spoint[0]) * spoint[1],
                     spoint[2]])
