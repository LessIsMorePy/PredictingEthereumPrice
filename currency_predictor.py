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

# Buil new DataFrame
new_df["Date"] = pd.to_datetime(df["Fecha"])
new_df["USD Value"] = df["Último"]
new_df["Float_USD_Value"] = df["Último"].apply(lambda x: float(x.replace('.', '').replace(',', '.')))

date = new_df['Date']
eth = new_df['Float_USD_Value']

# Set date
new_df.set_index("Date", inplace=True)

print("DataFrame:\n", df.head())
print("\nNew DF:\n", new_df.head())
print("\ndf shape:{}, new_df shape:{}".format(df.shape, new_df.shape))

# Plot
new_df.Float_USD_Value['2018-01-01': '2018-05-05'].plot(kind='area', alpha=0.4, color='blue')
plt.title("Ether value")
plt.ylabel("USD")
plt.show()

