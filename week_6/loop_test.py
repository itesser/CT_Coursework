import pandas as pd
import numpy as np

df_3 = pd.read_csv(r'acnh/accessories.csv')

df_3.columns = df_3.columns.str.lower().str.strip().str.replace(' ','_')

threshold = int(len(df_3)*.3)

col_to_drop = []
for column in df_3.columns:
    if df_3[column].nunique() >= 10:
        col_to_drop.append(column)
