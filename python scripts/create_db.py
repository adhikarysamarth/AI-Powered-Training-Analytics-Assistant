import pandas as pd
import sqlite3

df = pd.read_csv("./data/cleaned/cleaned_data.csv")

conn = sqlite3.connect("database/training_analytics.db")

df.to_sql("training_data", conn, if_exists="replace", index=False)

print("Loaded successfully")