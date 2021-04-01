
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

# * Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

data = pd.read_csv('student-mat.csv', sep=';')
def trans_famsup(x):
    if x == 'yes':
        return 1
    if x== 'no':
        return 0

data['alt_famsup']=data['famsup'].apply(trans_famsup)

# * Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program

data = data[['G1', 'G2', 'G3', 'absences', 'studytime', 'failures', 'alt_famsup']]

predict = 'G3'
# * Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# * streathing my knowledge using basic machine learning to predict outcomes

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

accuracy = linear.score(x_test, y_test)

prediction = linear.predict(x_test)

for x in range(len(prediction)):
    print(prediction[x], x_test[x], y_test[x])