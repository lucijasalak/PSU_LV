import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Učitavanje podataka ---
df = pd.read_csv('cars_processed.csv')
print(df.info())

# --- Scatter i pair plot ---
sns.pairplot(df, hue='fuel')
sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')

# --- Uklanjanje nepotrebnih stupaca ---
df = df.drop(['name', 'mileage'], axis=1)
# 1. Koliko mjerenja (automobila) je dostupno u datasetu?
num_measurements = df.shape[0]
print("Broj mjerenja (automobila):", num_measurements)

# 2. Kakav je tip pojedinog stupca u dataframeu?
column_types = df.dtypes
print("\nTipovi stupaca:\n", column_types)

# 3. Koji automobil ima najveću cijenu, a koji najmanju?
max_price_row = df.loc[df['selling_price'].idxmax()]
min_price_row = df.loc[df['selling_price'].idxmin()]
print("\nAutomobil s najvecom cijenom:\n", max_price_row)
print("\nAutomobil s najmanjom cijenom:\n", min_price_row)

# 4. Koliko automobila je proizvedeno 2012. godine?
cars_2012 = df[df['year'] == 2012].shape[0]
print("\nBroj automobila proizvedenih 2012.:", cars_2012)

# 5. Koji automobil je prešao najviše kilometara, a koji najmanje?
max_km_row = df.loc[df['km_driven'].idxmax()]
min_km_row = df.loc[df['km_driven'].idxmin()]
print("\nAutomobil s najvise kilometara:\n", max_km_row)
print("\nAutomobil s najmanje kilometara:\n", min_km_row)

# 6. Koliko najčešće automobili imaju sjedala?
most_common_seats = df['seats'].mode()[0]
print("\nNajcesci broj sjedala:", most_common_seats)

# 7. Prosječna prijeđena kilometraža po tipu goriva
avg_km_diesel = df[df['fuel'] == 'Diesel']['km_driven'].mean()
avg_km_petrol = df[df['fuel'] == 'Petrol']['km_driven'].mean()
print("\nProsjecna km za Diesel automobile:", avg_km_diesel)
print("Prosjecna km za Petrol automobile:", avg_km_petrol)

# --- Identifikacija tipova stupaca ---
obj_cols = df.select_dtypes(object).columns.tolist()
num_cols = df.select_dtypes(np.number).columns.tolist()

# --- Countplot za kategorijske stupce ---
fig = plt.figure(figsize=[15, 8])
for i, col in enumerate(obj_cols):
    plt.subplot(2, 2, i+1)
    sns.countplot(x=col, data=df)
    plt.title(f'Countplot of {col}')
plt.tight_layout()
plt.show()

# --- Boxplot za cijene po tipu goriva ---
df.boxplot(by='fuel', column=['selling_price'], grid=False)
plt.title('Boxplot of Selling Price by Fuel Type')
plt.suptitle('')  # uklanja defaultni naslov
plt.show()

# --- Histogram prodajnih cijena ---
df['selling_price'].hist(grid=False)
plt.xlabel('Selling Price')
plt.ylabel('Count')
plt.title('Histogram of Selling Price')
plt.show()

# --- Heatmap korelacije samo numeričkih stupaca ---
tabcorr = df[num_cols].corr()
plt.figure(figsize=(10,6))
sns.heatmap(tabcorr, annot=True, linewidths=1, cmap='coolwarm')
plt.title('Correlation Heatmap (Numerical Columns)')
plt.show()

import pandas as pd

