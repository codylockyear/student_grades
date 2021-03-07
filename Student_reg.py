
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv('student-mat.csv', sep=';')
def trans_famsup(x):
    if x == 'yes':
        return 1
    if x== 'no':
        return 0

data['alt_famsup']=data['famsup'].apply(trans_famsup)


data = data[['G1', 'G2', 'G3', 'absences', 'studytime', 'failures', 'alt_famsup']]

predict = 'G3'