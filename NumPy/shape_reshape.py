import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def shape_reshape():
    matrix = np.random.randint(1, 10, (3, 4))
    print(matrix.shape)
    print(matrix)
    print(matrix.reshape(1,12))
    print(np.reshape(matrix, (1,12)))
    #Reshape by rows 
    # [0][0]=>[0][1]=>[0][2]=>[0][3]=>
    # [1][0]=>[1][1]=>[1][2]=>[1][3]=>
    # [2][0]=>[2][1]=>[2][2]=>[2][3]
    print(np.reshape(matrix, (4,3), 'C'))
    # Order: 00 => 01 => 02 => 10 => 11 => 12 => 20 => 21 => 22 => 30 => 31 => 32
    #   00      30      21      12
    # [0][0]  [0][1]  [0][2]  [0][3]
    #   10      01      31      22
    # [1][0]  [1][1]  [1][2]  [1][3]
    #   20      11      02      32
    # [2][0]  [2][1]  [2][2]  [2][3]
    print(np.reshape(matrix, (4,3), 'F'))
    #Reshape by computer optimization
    print(np.reshape(matrix, (4,3), 'A'))