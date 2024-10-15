#%%
import random
from nltk.corpus import wordnet as wn
from datetime import datetime, timedelta
import pandas as pd

universe_id = 42
random.seed(universe_id)

class BigBang:
    def __init__(self):
        self.all_adjs = list(wn.all_synsets('a'))
        self.all_nouns = list(wn.all_synsets('n'))

    def generate_random_date(self, year, month):
        start_date = datetime(year, month, 1)
        end_date = start_date.replace(month=start_date.month % 12 + 1) - timedelta(days=1)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date.strftime('%Y-%m-%d')

    def generate_random_word(self, word_type):
        if word_type == 'adj':
            words = self.all_adjs
        elif word_type == 'noun':
            words = self.all_nouns
        return random.choice(words).lemmas()[0].name()

    def generate_random_name(self):
        adj = self.generate_random_word('adj').replace('_', ' ')
        noun = self.generate_random_word('noun').replace('_', ' ')
        name = f"{adj} {noun}"
        return name.title()

    def generate_random_number(self, start, end, number_type, decimal_places=0):
        if number_type == 'int' or number_type == int:
            return random.randint(start, end)
        elif number_type == 'float' or number_type == float:
            # return round(random.uniform(start, end), decimal_places)
            return round(start + (end - start) * random.betavariate(1, 2), decimal_places)
        else:
            raise ValueError(f"Unknown number type: {number_type}")

    def generate_column_dict(self, column_specs):
        column_dict = {}
        for spec in column_specs:
            if spec['type'] == 'number':
                if spec['number_type'] == float or spec['number_type'] == 'float':
                    column_dict[spec['name']] = (self.generate_random_number, [spec['start'], spec['end'], spec['number_type'], spec['decimal_places']])
                else:
                    column_dict[spec['name']] = (self.generate_random_number, [spec['start'], spec['end'], spec['number_type']])
            elif spec['type'] == 'date':
                column_dict[spec['name']] = (self.generate_random_date, [spec['year'], spec['month']])
            elif spec['type'] == 'name':
                column_dict[spec['name']] = (self.generate_random_name, [])
        return column_dict

    def generate_random_data(self, column_dict, n_rows, filename=None):
        data = {}
        for column, (func, args) in column_dict.items():
            data[column] = [func(*args) for _ in range(n_rows)]
        df = pd.DataFrame(data)
        if filename:
            df.to_csv(filename, index=False)
        else:
            return df


class BigFreeze(BigBang):
    def __init__(self):
        super().__init__()
    
    def generate_random_data(self, column_dict, n_rows, filename=None):
        df = super().generate_random_data(column_dict, 0)
        # add empty rows
        df.loc[len(df)] = [None] * len(df.columns)
        if filename:
            df.to_csv(filename, index=False)
        else:
            return df
    
    

if __name__ == '__main__':
    big_bang = BigBang()
    column_specs = [
        {'name': 'id', 'type': 'number', 'start': 10**5, 'end': 10**12-1, 'number_type': 'int', 'decimal_places': 0},
        {'name': 'customer', 'type': 'name'},
        {'name': 'sale_date', 'type': 'date', 'year': 1988, 'month': 5},
        {'name': 'days_in_inventory', 'type': 'number', 'start': 1, 'end': 42, 'number_type': 'int', 'decimal_places': 0},
        {'name': 'count', 'type': 'number', 'start': 1, 'end': 42, 'number_type': 'int', 'decimal_places': 0},
        {'name': 'price', 'type': 'number', 'start': 0, 'end': 42, 'number_type': 'float', 'decimal_places': 2},
    ]
    big_bang.generate_random_data(big_bang.generate_column_dict(column_specs), 100, 'input/random_data.csv')
#%%
