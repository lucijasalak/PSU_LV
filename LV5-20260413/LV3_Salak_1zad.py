import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ucitaj podatke za ucenje
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

#b
print(len(df))
#c
print(df[target_name].value_counts())

# Scatter plot
plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()

'''a) dio
-Kada je CO2 veci, prostorija je cesce zauzeta
-Kada je CO2 manji, prostorija je cesce slobodna
-CO2 je jaci indikator od temperature '''