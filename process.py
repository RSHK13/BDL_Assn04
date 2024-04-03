import pandas as pd
import numpy as np
from ruamel.yaml import YAML


def compute_aggregate(df):
    Monthly_data = []
    for i in range(12):
        Monthly_data.append([])
    for i in range(len(df)):

        date_str = df['DATE'][i]
        month_str = date_str[5:7]
        month = eval(month_str[1]) if month_str[0] =='0' else eval(month_str)
        temp = df['HourlyDryBulbTemperature'][i]
        if(isinstance(temp, str) and temp[-1] == 's'):
            temp = temp[:len(temp)-1]
        if(np.isnan(float(temp))):
            Monthly_data[month - 1].append(0)
        else:
            Monthly_data[month - 1].append(float(temp))
    Monthly_avg = []
    for month in Monthly_data:
        Monthly_avg.append(np.mean(np.array(month)))
    Monthly_avg_df = pd.DataFrame({'predicted_Monthly_mean' : Monthly_avg})
    Monthly_avg_df.to_csv('data/predicted_Monthly_mean.csv', index=False)

def convert_to_df(file_idx):
    df = pd.read_csv(f'data/csv_{file_idx}.csv', dtype="str")
    return df

if __name__ == '__main__':
    yaml = YAML(typ="safe")
    params = yaml.load(open("params.yaml", encoding="utf-8"))
    df = convert_to_df(file_idx=params['process']['num_files'])
    compute_aggregate(df)