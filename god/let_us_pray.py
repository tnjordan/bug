#%%
#TODO: https://gideonbrimleaf.github.io/2021/01/26/relative-imports-python.html
import sys
print(sys.path[1])

import os
print(os.getcwd())

# export PYTHONPATH="${PYTHONPATH}:/home/todd/temp/bug"

import math
import random
from datetime import datetime
from god.creation import BigBang, BigFreeze


bb = BigBang()
bf = BigFreeze()

# Get the current year and month
current_year = datetime.now().year
current_month = datetime.now().month

years = 2
# Iterate over the past 'years' years
for year in range(current_year - years, current_year + 1):
    # Iterate over each month
    for month in range(1, 13):
        # If the current year and month is reached, break the loop
        if year == current_year and month >= current_month:
            break
        factor_of_sin = ((math.sin(month * math.pi / 6)+1)/2+1)
        column_specs = [
            {'name': 'id', 'type': 'number', 'start': 10**11, 'end': 10**12-1, 'number_type': 'int'},
            {'name': 'customer', 'type': 'name'},
            {'name': 'sale_date', 'type': 'date', 'year': year, 'month': month},
            {'name': 'days_in_inventory', 'type': 'number', 'start': 1, 'end': 42, 'number_type': 'int'},
            {'name': 'count', 'type': 'number', 'start': 1, 'end': int(88*factor_of_sin), 'number_type': 'int'},
            {'name': 'price', 'type': 'number', 'start': 88, 'end': 512*factor_of_sin, 'number_type': 'float', 'decimal_places': 2},
        ]
        bb.generate_random_data(bb.generate_column_dict(column_specs), int(88 + (512 - 88) * random.betavariate(1, 2)), f'input/{year}_{month}_sales.csv')

bf.generate_random_data(bf.generate_column_dict(column_specs), 100, f'input/{year}_{month}_sales.csv')

#%%
