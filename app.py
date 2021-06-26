# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:15:11 2021

@author: PRAMILA
"""

import streamlit as st
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
pickle.dump(rand_forest, open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))


models = pickle.load(open('model.pkl', 'rb'))
def home():
    return "welcome"


def predict(cgpa,arrear):
    prediction = models.predict([[cgpa,arrear]])
    print(prediction)
    return prediction

def main():
    st.title("STUDENT PLACEMENT PREDICTION⭐")
    st.header('STUDENT DETAILS💻')
    studentname = st.text_input('Name 📋')
    regno= st.text_input('Register Number 📋')
    dep= st.text_input('Department 📋')
    cgpa=st.number_input('CGPA',min_value=0.0,max_value=10.0,value=0.0,step=0.5) 
    arrear=st.number_input('Number of Arrears',min_value=0,max_value=50,value=0,step=1) 
    st.radio("Interest about placement ✔️", ('Interested', 'Not Interested'))

    result = ""
    if st.button("Submit"):
        result = predict(cgpa,arrear)
        print(result)
    

        st.subheader("Entered Details")
        st.write("Name 📋 : ", studentname)
        st.write("Register Number 📋 :", regno)
        st.write("CGPA 🎓 :", cgpa)
        st.write("Number of Arrears :", arrear)
        if(result==[0]):
           st.success('Predicted Results:- Not placed'.format(result)) 
        else:
          st.success('Predicted Results:- You will be Placed with approx Rs.{} per annum'.format("%.1f" % result))
        
  
    
if __name__ == "__main__":
    main()
