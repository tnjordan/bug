import random
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
        self.init()

    @staticmethod
    def extract_customer(ds):
        def get_capital_and_next_vowel(input_string):
            vowels = 'AEIOU'
            result = []
            for i in range(len(input_string)):
                if input_string[i].isupper():
                    if input_string[i] not in vowels:
                        for j in range(i+1, len(input_string)):
                            if input_string[j].upper() in vowels:
                                result.append(input_string[i] + input_string[j])
                                break
                        else:
                            result.append(input_string[i])
                    else:
                        result.append(input_string[i])
            return ''.join(result)
        def palindrome(s):
            return s + s[::-1]
        def drop_double_lower_vowels(s):
            vowels = 'AEIYOU'
            result = [s[i] for i in range(len(s)) if s[i].isupper() or 
                        (s[i] in vowels and 
                        (i == 0 or s[i-1] != s[i]) and 
                        (i == len(s) - 1 or s[i+1] != s[i]))]
            return ''.join(result)
        return ds.apply(lambda x: get_capital_and_next_vowel(x)).apply(lambda x: drop_double_lower_vowels(x)).apply(lambda x: palindrome(x))

    @staticmethod
    def fix_id(df):
        df['id'] = df['id'].astype(str).apply(lambda x: x[::-1])
        df['id'] = df['id'].zfill(12)
        df['id'] = df['id'].astype(int)
        return df['id']
    
    @staticmethod
    def fix_sale_date(df):
        day = df['sale_date'].apply(lambda x: int(x.split('-')[2]))
        days_in_month = df['sale_date'].apply(lambda x: int(x.split('-')[1]))
        days_in_month = days_in_month.apply(lambda x: 30 if x in [4, 6, 9, 11] else 31 if x in [1, 3, 5, 7, 8, 10, 12] else 28)
        day = day + df['days_in_inventory'] % days_in_month
        df['new_sale_date'] = df['sale_date'].apply(lambda x: x.split('-')[0]) + '-' +  df['sale_date'].apply(lambda x: x.split('-')[1]) + '-' + day.astype(str)
        return df['new_sale_date']

    @staticmethod
    def calculate_inventory_date(df):
        #TODO
        df['inventory_date'] = None
        pass

    @staticmethod
    def fix_sale_price(df):
        df_price = df[['price', 'count']]
        df_price['unit'] = df_price['price'] / df_price['count']
        df_price['price'] = round(df_price['unit'], 2) * df_price['count']
        return df_price['price']
    
    def fix(self, df):
        df['customer'] = self.extract_customer(df['customer'])
        df['sale_date'] = self.fix_sale_date(df)
        df['inventory_date'] = self.calculate_inventory_date(df)
        df['price'] = self.fix_sale_price(df)
        return df

    def init(self, n=1):
        b = ""
        for i in range(n):
            b += random.choice(list(self.__dict__.values()))
            print(b[-1]*(i+1))
