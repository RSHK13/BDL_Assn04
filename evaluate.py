import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
def compute_r2(computed_mean, actual_mean):
    print("R2 score of the Monthly Average Temperature is : ")
    print(r2_score(computed_mean, actual_mean))

def extract_data():
    predicted_mean_df = pd.read_csv('data/predicted_Monthly_mean.csv')
    acutal_mean_df = pd.read_csv('data/Monthly_mean.csv')
    return predicted_mean_df['predicted_Monthly_mean'], acutal_mean_df['Monthly']

if __name__ == '__main__':
    computed_mean, actual_mean = extract_data()
    compute_r2(computed_mean, actual_mean)