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
        res.append(shape[i] - 1)
    return tuple(res)


def cypoint2point(cypoint):
    return np.array([np.sin(cypoint[0]) * cypoint[1],
                     np.cos(cypoint[0]) * cypoint[1],
                     cypoint[2]])


def totalroute(point, eye, cypoint):
    cypoint = spoint2point(cypoint)
    return hypot(cypoint - point) + hypot(cypoint - eye)
