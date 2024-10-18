import pandas as pd
import random
import calendar
from decimal import Decimal, ROUND_UP
import re
from src.utils import *

class DataProcessor:
    def __init__(self):
        self.lady = "🐞"
        self.worm = "🐛"
        self.butterfly = "🦋"
        self.bee = "🐝"
        self.ant = "🐜"
        self.snail = "🐌"
        self.grasshopper = "🦗"
        self.spider = "🕷️"
        self.scorpion = "🦂"

    @staticmethod
    def extract_customer(ds):
        def get_capital_and_next_vowel(input_string):
            vowels = 'AEIYOU'
            result = []
            
            # encoding is done per word, split compound words
            input_strings = re.split(' |-', input_string)
            for word in input_strings:
                for i in range(len(word)):
                    if word[i].isupper():
                        if word[i] not in vowels:
                            for j in range(i+1, len(word)):
                                if word[j].upper() in vowels:
                                    result.append(word[i] + word[j])
                                    break
                            else:
                                result.append(word[i])
                        else:
                            result.append(word[i])
            return ''.join(result)

        def palindrome(s):
            return s + s[::-1]

        def drop_double_lower_vowels(s):
            vowels = 'aeiyou'
            result = [s[i] for i in range(len(s)) if s[i].isupper() or 
                        (s[i] in vowels and 
                        (i == 0 or s[i-1] != s[i]) and 
                        (i == len(s) - 1 or s[i+1] != s[i]))]
            return ''.join(result)

        ds_extract = ds.apply(lambda x: get_capital_and_next_vowel(x))
        ds_extract = ds_extract.apply(lambda x: palindrome(x))  # palindrome first or no double lower vowels
        ds_extract = ds_extract.apply(lambda x: drop_double_lower_vowels(x))
        return ds_extract


    @staticmethod
    def fix_id(ds):
        ds = ds.copy()
        # reverse string
        ds = ds.astype(str).apply(lambda x: x[::-1])
        # remove leading zeros
        ds = ds.apply(lambda x: x.lstrip('0'))
        # pad with zeros to keep 12 characters
        ds = ds.apply(lambda x: x.ljust(12,'0'))
        ds = ds.astype(int)
        return ds
    
    @staticmethod
    def fix_sale_date(df):
        df = df.copy()
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        # get year, month, day into separate columns
        df['year'] = df['sale_date'].dt.year
        df['month'] = df['sale_date'].dt.month
        df['old_day'] = df['sale_date'].dt.day  # if pd.to_datetime needed year, month, day columns
        df['days_in_month'] = df['sale_date'].apply(lambda x: calendar.monthrange(x.year, x.month)[1])
        # calculate actual day, and account for boundary case of % == 0 should be last day of month
        df['day'] = (df['old_day'] + df['days_in_inventory']) % df['days_in_month']
        df['day'] = df['day'].where(df['day'] != 0, df['days_in_month'])
        # create new sale date
        df['new_sale_date'] = pd.to_datetime(df[['year', 'month', 'day']])
        return df['new_sale_date']

    @staticmethod
    def calculate_inventory_date(df):
        df = df.copy()
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        df['inventory_date'] = df['sale_date'] - pd.to_timedelta(df['days_in_inventory'], unit='d')
        return df['inventory_date']

    @staticmethod
    def fix_sale_price(df):
        df_price = df[['price', 'count']].copy()
        df_price['unit'] = df_price.apply(lambda row: Decimal(row['price']) / Decimal(row['count']), axis=1)
        df_price['fixed_unit'] = df_price['unit'].apply(lambda x: x.quantize(Decimal('0.01'), rounding=ROUND_UP))
        df_price['fixed_price'] = df_price.apply(lambda row: row['fixed_unit'] * Decimal(row['count']), axis=1)
        df_price['fixed_price'] = df_price['fixed_price'].astype(float)  # sqlite does not support Decimal
        return df_price['fixed_price']
    
    def fix(self, df):
        df['id'] = self.fix_id(df['id'])
        df['customer'] = self.extract_customer(df['customer'])
        df['sale_date'] = self.fix_sale_date(df)
        df['inventory_date'] = self.calculate_inventory_date(df)
        df['price'] = self.fix_sale_price(df)
        df.columns = [col.upper() for col in df.columns]  # make all columns uppercase for SQL standard
        return df

    def plague(self, n):
        infestation = ""
        for i in range(n):
            infestation += random.choice(list(self.__dict__.values()))
            print(infestation[-1]*i)
        return infestation
