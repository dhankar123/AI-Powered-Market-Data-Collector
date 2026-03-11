import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="market_data",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

df = pd.read_csv("data/processed/books_clean.csv")

for index,row in df.iterrows():
    cursor.execute(
        "INSERT INTO products (product_name,price) VALUES (%s,%s)",
        (row['product_name'],row['price'])
    )

conn.commit()
cursor.close()
conn.close()