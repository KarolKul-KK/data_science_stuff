from typing import List
import math


Vector = List[float]
height_weight_age = [170,
                    70,
                    40]

rate = [95,
        80,
        75,
        65]


def add(v: Vector, w: Vector) -> Vector:
    # addition
    assert len(v) == len(w), 'vectors must have the same length'
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6])


def subtract(v: Vector, w: Vector) -> Vector:
    # subtraction
    assert len(v) == len(w), 'vector must have the same length'
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    # sum of all vectors from list
    # check the value of list is not 0
    assert vectors, 'Empty list of vectors'

    # check length of all vectors
    num_elements = len(vectors[0])
    assert all (len(v) == num_elements for v in vectors), 'different length'

    # i-ty element of final vector is sum of elements[i] every vector
    return [sum(vector[i] for vector in vectors)
        for i in range(num_elements)]

    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    # Multiply every element by c
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    # calculate vector which i-ty element is mean i-ty elements final vectors
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    # calculate v_1 * w_1 * ... * v_n * w_n
    assert len(v) == len(w), "vectors must be the same"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    # return v_1 * v_1 * ... * v_n * v_n
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14 


def magnitude(v: Vector) -> float:
    # return module of vector v
    return math.sqrt(sum_of_squares(v)) # math.sqrl calculate value of square root

assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    # calculate (v_1 - w_1)**2 + ... + (v_n - w_n)**2
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    # calculate distance between v and w
    return magnitude(subtract(v, w))

