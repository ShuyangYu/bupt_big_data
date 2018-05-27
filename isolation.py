import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import numpy as np

data = pd.read_csv('network_record_day_class.csv')
data.head()

rng = np.random.RandomState(42)
clf = IsolationForest(max_samples=100, random_state=rng)

clf.fit(data['total_class'].reshape(-1, 1))

y_pred_train = clf.predict(data['total_class'].reshape(-1, 1))

y_pred_train[:50]