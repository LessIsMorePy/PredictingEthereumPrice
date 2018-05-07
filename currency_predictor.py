# Modules
import glob
import pandas as pd
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Rate USD  MXN
try:
    dollar_price = CurrencyRates().get_rate('USD', 'MXN')
except:
    print("Internet error connection, what is the dollar price?")
    dollar_price = float(input("Dollar price: "))

# Save all file matches
csv_files = glob.glob("*.csv")

# Read csv file
df = pd.read_csv(csv_files[0])
assert pd.notnull(df).all().all()
new_df = pd.DataFrame()

new_df["Date"] = pd.to_datetime(df["Fecha"])
new_df["USD Value"] = df["Último"]
new_df["Float USD Value"] = df["Último"].apply(lambda x: float(x.replace('.', '').replace(',', '.')))
new_df["MXN"] = new_df["Float USD Value"].apply(lambda x: x * dollar_price)

new_df.set_index("Date", inplace=True)

print("DataFrame:\n", df.head())
print("\nNew DF:\n", new_df.head())
print("\nSummary statistics:\n", new_df.MXN.describe())
print("\ndf shape:{}, new_df shape:{}".format(df.shape, new_df.shape))

"""
new_df.MXN['2018-01-01': '2018-05-05'].plot()
plt.title("Ether value")
plt.ylabel("MXN")
plt.show()
"""
