#%%
# make function to upload csv file to a table
import sqlite3
import pandas as pd
from src.data_processor import DataProcessor

def read_csv(csv_file):
    return pd.read_csv(csv_file)

def upload_csv_to_table(db_name, table_name, csv_file):
    conn = sqlite3.connect(db_name)
    data = read_csv(csv_file)
    dp = DataProcessor()
    data = dp.fix(data)
    data.to_sql(table_name, conn, if_exists='append', index=False)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    conn.commit()
    conn.close()
    return df

def read_table(db_name, table_name):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    conn.close()
    return df

#%%
# df = upload_csv_to_table('bases/example.db', 'SALES', 'input/20221_sales.csv')
# df
#%%
