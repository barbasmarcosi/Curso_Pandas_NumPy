import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def data_types():
    new_arr = np.arange(10)
    print(new_arr.dtype)
    print(new_arr)
    # Change to array and data type to float 64
    # new_arr = np.array(new_arr, dtype=np.float64)
    new_arr = new_arr.astype(np.float64)
    print(new_arr.dtype)
    print(new_arr)
