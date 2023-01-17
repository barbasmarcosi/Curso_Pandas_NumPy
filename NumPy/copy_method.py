import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def copy_method():
    vector = np.arange(0,11)
    vector_2 = np.copy(vector[:6])
    vector_2[:] = 0
    print(vector)
    print(vector_2)
