import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def operations():
    vector = np.arange(0, 10)
    vector_2 = np.copy(vector)
    print(vector * 2)
    print(vector + vector_2)
    matrix = np.random.randint(0, 10, (10, 10))
    matrix_2 = np.copy(matrix)
    print(matrix)
    print(matrix * 2)
    print(np.matmul(matrix, matrix_2))
    print(matrix @ matrix_2)