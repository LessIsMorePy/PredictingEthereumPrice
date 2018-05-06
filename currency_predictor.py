# Modules
import glob
import pandas as pd

# Save all file matches
csv_files = glob.glob("*.csv")

# Read csv file
df = pd.read_csv(csv_files[0])
new_df = pd.DataFrame()

new_df["Date"] = df["Fecha"]
new_df["USD Value"] = df["Último"]
new_df["Float USD Value"] = df["Último"].apply(lambda x: float(x.replace('.', '').replace(',', '.')))

print("DataFrame:\n", df.head())
print("New DF:\n", new_df.head())