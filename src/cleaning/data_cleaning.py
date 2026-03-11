import pandas as pd
df = pd.read_csv("data/raw/books_raw.csv")
df['price'] = (
    df['price']
    .str.replace('£', '', regex=False)       # remove £
    .str.replace(r'[^\d\.]', '', regex=True) # remove stray non-numeric chars
    .astype(float)                           # convert to float
)
df.drop_duplicates(inplace=True)
df.to_csv("data/processed/books_clean.csv",index=False)