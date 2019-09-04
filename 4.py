import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

dataBoston =  load_boston()
# print(dataBoston)
# 'DESCR' , 'data', 'feature_names', 'filename', 'target'
# print(dir(dataBoston))
# print(dataBoston['data'][0])
# print(dataBoston['feature_names'])
# print(dataBoston['target'])

df  =  pd.DataFrame(
    dataBoston['data'],
    columns = dataBoston['feature_names']
)

print(df)