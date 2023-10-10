import pandas as pd

tit_df = pd.read_csv('https://raw.githubusercontent.com/lucchesia7/coding-temple-da-sql-day-1/main/day_1/data/titanic.csv')
tit_df.columns = tit_df.columns.str.lower().str.replace('/','_').str.strip()

connection = 'postgresql://wswxlbyo:FkgqQF0gFkb3bXQoXH-HA9n432CcGUTG@bubble.db.elephantsql.com/wswxlbyo'
tit_df.to_sql('titanic', con = connection, if_exists='replace')

# titanic_hw.sql