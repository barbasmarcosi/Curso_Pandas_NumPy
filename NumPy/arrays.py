import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def arrays():
    main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = np.array(main_list)
    matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5,
                                                  6, 7, 8, 9], [3, 2, 6, 4, 6, 7, 8, 9]])
    print(matrix)
    print(matrix.shape)
    print(matrix[::2, ::2])

    # Second part
    print('\nSecond part:\n')
    # np.arange (Start,End,Steps)
    print(np.arange(0, 10, 2))
    # np.zeros
    print(np.zeros((10, 10, 10)))
    # np.ones
    print(np.ones((3, 3, 3)))
    # np.linspace(Min, Max, Shape): Linear distribution in range of numbers win min and max values
    print(np.linspace(0, 10, 100))
    # np.eye(Number of rows and columns): Identity matrix
    print(np.eye(5))
    # np.random.rand
    print(np.random.rand(10, 10))
    # np.random.randint (Min, Max, Shape)
    print(np.random.randint(0, 10, 10))
    print(np.random.randint(0, 10, (10, 10)))