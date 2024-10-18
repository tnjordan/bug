import sqlite3
import argparse
from typing import Dict, List, Tuple, Union

class DatabaseVerifier:
    def __init__(self, db_path, table):
        self.db_path = db_path
        self.table = table
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def run_query_and_verify(self, query, expected_result):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result == expected_result:
                print("✔️")
            else:
                print("❌")
                print(f"?: {query}")
                print(f"Expected: {expected_result}")
                print(f"Got: {result}")
        except sqlite3.Error as e:
            print(f"🔥 An SQLite error occurred: {e}")
        except Exception as e:
            print(f"🔥 An unexpected error occurred: {e}")

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
                print("Connection closed.")
        except sqlite3.Error as e:
            print(f"An error occurred while closing the connection: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while closing the connection: {e}")

    def test(self):
        # dictionary of queries and expected results
        queries: Dict[str, List[Tuple[Union[int, float]]]] = {
            f"PRAGMA table_info({self.table})": [   (0, 'ID', 'INTEGER', 0, None, 0),
                                                    (1, 'CUSTOMER', 'TEXT', 0, None, 0),
                                                    (2, 'SALE_DATE', 'TIMESTAMP', 0, None, 0),
                                                    (3, 'DAYS_IN_INVENTORY', 'INTEGER', 0, None, 0),
                                                    (4, 'COUNT', 'INTEGER', 0, None, 0),
                                                    (5, 'PRICE', 'REAL', 0, None, 0),
                                                    (6, 'INVENTORY_DATE', 'TIMESTAMP', 0, None, 0)],
            f"SELECT COUNT(*) FROM {self.table} WHERE ID = 887473209070;": [(1,)],
            f"SELECT SUM(COUNT) FROM {self.table} WHERE customer = 'ASSA';": [(3301,)],
            f"SELECT 1 FROM {self.table} WHERE CUSTOMER = 'TiWiNNiWiT' LIMIT 1;": [(1,)],
            f"SELECT SUM(COUNT) FROM {self.table} WHERE SALE_DATE BETWEEN '2023-05-12' AND '2024-06-17';": [(202237,)],
            f"SELECT ROUND(SUM(PRICE), 2) FROM {self.table} WHERE SALE_DATE BETWEEN '2023-05-12' AND '2024-06-17';": [(961294.27,)],
            f"SELECT COUNT(*) FROM {self.table} WHERE SALE_DATE BETWEEN '2023-01-13' AND '2024-02-13';": [(2539,)],
            f"SELECT MAX(ID) - MIN(ID) FROM {self.table};": [(899992431308,)],
            f"SELECT COUNT(*) FROM {self.table} WHERE INVENTORY_DATE BETWEEN '2023-01-13' AND '2024-02-13';": [(2532,)],
            f"SELECT SUM(ID) FROM {self.table} WHERE strftime('%Y-%m', SALE_DATE) = '2024-09';": [(155611881639154,)],
            f"SELECT COUNT(*) FROM {self.table} WHERE CUSTOMER = 'OKKO';": [(2,)],
            f"SELECT ROUND(SUM(PRICE), 2) FROM {self.table} WHERE strftime('%m-%d', INVENTORY_DATE) = '09-10' AND strftime('%Y', INVENTORY_DATE) IN ('2023', '2024');": [(3198.49,)],
            f"SELECT COUNT(*) FROM {self.table} WHERE PRICE > 555;": [(786,)],
            f"SELECT MIN(SALE_DATE) FROM {self.table};": [('2022-01-01 00:00:00',)],
            f"SELECT MAX(PRICE / COUNT) AS UNIT_PRICE FROM {self.table};": [(792.25,)],
            f"SELECT MAX(SALE_DATE) FROM {self.table};": [('2024-09-30 00:00:00',)],
            f"SELECT COUNT(*) FROM {self.table} WHERE CUSTOMER = 'IAAI';": [(23,)],
            f"SELECT MIN(INVENTORY_DATE) FROM {self.table};": [('2021-11-21 00:00:00',)],
            f"SELECT MAX(INVENTORY_DATE) FROM {self.table};": [('2024-09-26 00:00:00',)],
            f"SELECT MAX(ID) FROM {self.table};": [(999995413204,)],
            f"SELECT CUSTOMER FROM {self.table} ORDER BY LENGTH(CUSTOMER) DESC LIMIT 1;": [('PaPoFoFoTeLiOPaGeCCeGaPOiLeToFoFoPaP',)],
            f"SELECT SUM(DAYS_IN_INVENTORY) FROM {self.table};": [(156486,)],
            f"SELECT ROUND(SUM(PRICE),2) FROM {self.table} WHERE strftime('%Y-%m', SALE_DATE) = '2024-03';": [(77725.35,)],
            f"SELECT SUM(PRICE) FROM (SELECT PRICE FROM {self.table} ORDER BY PRICE DESC LIMIT 3);": [(2913.25,)],
            f"SELECT SUM(PRICE) FROM (SELECT PRICE FROM {self.table} ORDER BY PRICE ASC LIMIT 3);": [(264.86,)],
            f"SELECT PRICE FROM {self.table} WHERE ID = 445170166202;": [(111.09,)],
            f"SELECT MIN(PRICE / COUNT) AS UNIT_PRICE FROM {self.table};":  [(0.55,)],
        }
        for q,a in queries.items():
            self.run_query_and_verify(q, a)

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Verify database query results.')
    parser.add_argument('db_path', type=str, help='Path to the SQLite database file')
    parser.add_argument('table', type=str, help='Name of the table to query')

    args = parser.parse_args()
    
    db_verifier = DatabaseVerifier(args.db_path, args.table)
    db_verifier.test()
    db_verifier.close_connection()