#%%
import os
from src.create_db import upload_csv_to_table, read_table
import sqlite3

DB = 'bases/DATAVILLE.db'
TABLE = 'SALES'

def reset(DB, TABLE):
    conn = sqlite3.connect(DB)
    conn.execute(f'DROP TABLE IF EXISTS {TABLE}')
    conn.commit()
    conn.close()
reset(DB, TABLE)

for f in os.listdir('input'):
    print('File:', f)
    if f.endswith('.csv'):
        upload_csv_to_table(DB, TABLE, f'input/{f}')
        print(f'\tUploaded!')
#%%
