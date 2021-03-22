from typing import List


Vector = List[float]
height_weight_age = [170,
                    70,
                    40]

rate = [95,
        80,
        75,
        65]


def add(v: Vector, w: Vector) -> Vector:
    # sum of vectors
    assert len(v) == len(w), 'vectors must have the same length'
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6])


def subtract(v: Vector, w: Vector) -> Vector:
    # subtraction
    assert len(v) == len(w), 'vector must have the same length'
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]