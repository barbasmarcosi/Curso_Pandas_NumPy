import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def series_dataframes():
    print(pd.Series(['Navas', 'Mbappe', 'Neymar',
          'Messi'], index=[1, 7, 10, 30]))
    print(pd.Series({1: 'Navas', 7: 'Mbappe', 10: 'Neymar',
                     30: 'Messi'}))
    dictionary = {'Player': ['Navas', 'Mbappe', 'Neymar',
                             'Messi'], 'Heigth': [183, 176, 172, 170], 'Goals': [2, 25, 32, 52]}
    print(pd.DataFrame(dictionary, index=[1, 7, 10, 30]))