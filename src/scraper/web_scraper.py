import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

books = soup.find_all('article')

data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p',class_='price_color').text
    
    data.append({
        "product_name":title,
        "price":price
    })

df = pd.DataFrame(data)

df.to_csv("data/raw/books_raw.csv",index=False)