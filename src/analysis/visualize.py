import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/books_clean.csv")

df['price'].hist()

plt.show()