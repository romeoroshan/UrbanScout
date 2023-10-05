from joblib import load
import numpy as np
potential_model=load('us/player model/ability_model1.joblib')
input_data = [[19,100,100,100,100,100,100]]

predictions = potential_model.predict(input_data)
scaled_prediction = (predictions / 95) * 5

rounded_prediction = np.round(scaled_prediction).astype(int)
print(rounded_prediction)