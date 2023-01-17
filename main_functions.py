import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main_functions():
    vector = np.random.randint(1, 20, 10)
    print(vector)
    print(vector.max())
    matrix = vector.reshape(2, 5)
    print(matrix)
    print(matrix.max())
    # max(Axis): 0 is for maximum number for each column and 1 is for maximum number for each row
    print(matrix.max(0))
    print(matrix.max(1))
    # argmax(Axis): 0 is for maximum number for each column and 1 is for maximum number for each row
    # returns the indexes of the maximum values
    print(matrix.argmax(0))
    print(matrix.argmax(1))
    # max(Axis): 0 is for minium number for each column and 1 is for minium number for each row
    print(matrix.min(0))
    print(matrix.min(1))
    # argmax(Axis): 0 is for minium number for each column and 1 is for minium number for each row
    # returns the indexes of the minium values
    print(matrix.argmin(0))
    print(matrix.argmin(1))
    # ptp(Axis): 0 is for the absolute difference between maximum and minimum value for each column and 1 is for the absolute difference between maximum and minimum value for each row
    print(matrix.ptp())
    print(matrix.ptp(0))
    print(matrix.ptp(1))
    # np.percentile(array, percentage)
    print(np.percentile(matrix, 50))
    # np.median(array)
    print(np.median(matrix))
    # np.mean(array)
    print(np.mean(matrix))
    # np.std(array)
    print(np.std(matrix))
    # np.var(array))
    print(np.var(matrix))
    # sort(): returns the same array or matrix but in ascending order
    print(np.sort(vector))
    print(np.sort(matrix))
    # concatenate()
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a.ndim)
    b = np.array([[10, 11, 12], [13, 14, 15]])
    print(np.concatenate((a, b.T), axis=1))
    complete = np.array([np.zeros(3, dtype=np.int32)])
    print(complete)
    print(b)
    print(np.concatenate((a, b), axis=0))
    b = np.concatenate((b, complete), axis=0)
    print(b)
    print(np.concatenate((a, b), axis=1))
