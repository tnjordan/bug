import pandas as pd
import random

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
            vowels = 'AEIOU' #! AEIYOU
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
            vowels = 'AEIYOU' #! 'aeiyou'
            result = [s[i] for i in range(len(s)) if s[i].isupper() or 
                        (s[i] in vowels and 
                        (i == 0 or s[i-1] != s[i]) and 
                        (i == len(s) - 1 or s[i+1] != s[i]))]
            return ''.join(result)
        return ds.apply(lambda x: get_capital_and_next_vowel(x)).apply(lambda x: drop_double_lower_vowels(x)).apply(lambda x: palindrome(x))

    @staticmethod
    def fix_sale_date(df):
        # df['inventory_date'] = df['sale_date']  #! ha again #* never mind let us not reference the inventory_date they can calculate that later
        day = df['sale_date'].apply(lambda x: int(x.split('-')[2]))
        days_in_month = df['sale_date'].apply(lambda x: int(x.split('-')[1]))
        days_in_month = days_in_month.apply(lambda x: 30 if x in [4, 6, 9, 11] else 31 if x in [1, 3, 5, 7, 8, 10, 12] else 28)  #* fuck february, what a great bug make sure we go over a leap year
        
        day = day + df['days_in_inventory'] % days_in_month
        
        # solution 
        # new_day = (current_day + days_to_add) % days_in_month
        # if new_day == 0:
        #     new_day = days_in_month
        
        #* a good spot to mix and match types
        df['sale_date'] = df['sale_date'].apply(lambda x: x.split('-')[0]) + '-' +  df['sale_date'].apply(lambda x: x.split('-')[1]) + '-' + day.astype(str)
        
        # import calendar
        # df['sale_date'] = pd.to_datetime(df['sale_date'])
        # df['days_in_month'] = df['sale_date'].apply(lambda x: calendar.monthrange(x.year, x.month)[1])
        
        return df['sale_date']

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

    def plague(self, n):
        infestation = ""
        for i in range(n):
            infestation += random.choice(list(self.__dict__.values()))
            print(infestation[-1]*i)
        return infestation
