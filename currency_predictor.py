# Modules
import glob
import pandas as pd

# Save all file matches
csv_files = glob.glob("*.csv")
df = pd.read_csv(csv_files[0])

usd_price = df["Último"]

print(df.head())
print(usd_price.head())