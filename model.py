import numpy as np
import pandas as pd
import pickle
dataset = pd.read_csv('datasetplace.csv')

dataset = dataset.drop('Sl. No.', axis=1)
dataset = dataset.drop('dep', axis=1)
dataset = dataset.drop('regno', axis=1)
dataset = dataset.drop('studentname', axis=1)
dataset = dataset.drop('Name of the Employeer', axis=1)
dataset = dataset.drop('Package', axis=1)


# selecting the features and labels
X = dataset.drop(columns=['Annual Package'])
Y=dataset.loc[:,['Annual Package']]
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
rand_forest = RandomForestClassifier()
rand_forest=rand_forest.fit(X_train,Y_train)
print(rand_forest.predict([[6,0]]))
pickle.dump(rand_forest, open('model1.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model1.pkl','rb'))
