# Modules
import glob
import pandas as pd
from forex_python.converter import CurrencyRates

# Rate USD  MXN
dolar_price = CurrencyRates().get_rate('USD', 'MXN')

# Save all file matches
csv_files = glob.glob("*.csv")

# Read csv file
df = pd.read_csv(csv_files[0])
new_df = pd.DataFrame()

new_df["Date"] = df["Fecha"]
new_df["USD Value"] = df["Último"]
new_df["Float USD Value"] = df["Último"].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
new_df["MXN"] = new_df["Float USD Value"].apply(lambda x: x * dolar_price)

print("DataFrame:\n", df.head())
print("\nNew DF:\n", new_df.head())