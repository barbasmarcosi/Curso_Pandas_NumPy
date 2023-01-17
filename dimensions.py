import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def dimensions():
    vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [
        4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

    print('vector')
    print(vector)
    print(vector.ndim)
    print(vector.shape)
    print('matrix')
    print(matrix)
    print(matrix.ndim)
    print(matrix.shape)
    print('tensor')
    print(tensor)
    print(tensor.ndim)
    print(tensor.shape)

    # Add dimensions
    tensor_10 = np.array(vector, ndmin=10)
    print('tensor_10')
    print(tensor_10)
    print(tensor_10.ndim)
    print(tensor_10.shape)

    # Expand dimensions
    tensor_11 = np.expand_dims(tensor_10, axis=0)
    print('tensor_11')
    print(tensor_11)
    print(tensor_11.ndim)
    print(tensor_11.shape)

    # Delete dimensions
    new_vector = np.squeeze(tensor_11)
    print('new_vector')
    print(new_vector)
    print(new_vector.ndim)
    print(new_vector.shape)