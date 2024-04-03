from curses import flash
import pandas as pd
import numpy as np
from ruamel.yaml import YAML

def extract_columns(df:pd.DataFrame):
    Monthly_mean = df['MonthlyMeanTemperature']
    means = []
    for mean in Monthly_mean:
        mean = float(mean)
        if not np.isnan(mean):
            means.append(mean)
    Monthly_df = {'Monthly' : means}
    Monthly_df = pd.DataFrame(Monthly_df)
    Monthly_df.to_csv('data/Monthly_mean.csv', index=False)

def convert_to_df(file_idx):
    df = pd.read_csv(f'data/csv_{file_idx}.csv', dtype="str")
    return df

if __name__ == '__main__':
    yaml = YAML(typ="safe")
    params = yaml.load(open("params.yaml", encoding="utf-8"))
    df = convert_to_df(file_idx=params['prepare']['num_files'])
    extract_columns(df)