
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

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

acc = linear.score(x_test, y_test)

print(acc)