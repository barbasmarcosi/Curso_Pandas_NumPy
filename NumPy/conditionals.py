import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def conditionals():
    vector = np.linspace(1, 10, 10, dtype='int8')
    print(vector)
    new_vector = vector[vector > 5]
    print(new_vector)

    matrix = np.where(np.random.randint(0,10,(10,10)) > 5, True, False)
    print(matrix)