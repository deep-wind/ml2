import pandas as pd
import pickle
dataframe = pd.read_csv('Placementsample1.csv')
def convert_to_int(word):
    word_dict = {'Good':1, 'Bad':0,'yes':1,'no':0,'completed':1,'none':0}
    return word_dict[word]
X=dataframe.loc[:,['comSkill','ssc_p','hsc_p','degree_p','No_certi','internships','etest_p','sports','placetest_p']]
y=dataframe.loc[:,['status']]
from sklearn.ensemble import RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=10,criterion='entropy')
#Fitting model with training data
regressor=regressor.fit(X, y)
# Saving model to disk
pickle.dump(regressor, open('final_model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[convert_to_int('Good'),69.6,68.4,78.3,5,80]]))
