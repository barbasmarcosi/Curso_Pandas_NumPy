import pandas as pd

def read_csv_json():
    print(pd.read_csv('./bestsellers.csv', sep=',', header=0))
