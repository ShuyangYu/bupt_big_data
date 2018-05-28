import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import numpy as np

data = pd.read_csv('feature_id_day.csv')
data = data.drop(labels=['Unnamed: 0'], axis=1)
data.head()

rng = np.random.RandomState(42)
clf = IsolationForest(max_samples=100, random_state=rng)

clf.fit(data.iloc[:, 2:])
 
y_pred_train = clf.predict(data.iloc[:, 2:])

pd.DataFrame(y_pred_train).to_csv('y_pred_train.csv')