

import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

#1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
sorted = mtcars.sort_values(by=['mpg'], ascending=False)
print("\nAutomobili s najvecom potrosnjom: ")
print(sorted['car'].head(5))  

#2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
cyl8 = mtcars[mtcars.cyl == 8].sort_values(by='mpg')
print("Automobili s 8 cilindara i najmanjom potrosnjom:")
print(cyl8['car'].head(3))

#3. Kolika je srednja potrošnja automobila sa 6 cilindara?
print("Srednja potrosnja automobila sa 6 cilindara: ")
print(mtcars[mtcars.cyl==6].mpg.mean())

#4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
print("Srednja potrosnja automobila s 4 cilindra: ")
print(mtcars[(mtcars.cyl==4) & (mtcars.wt>=2.000) & (mtcars.wt<=2.200)].mpg.mean())

#5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
amrm = mtcars['am'].value_counts()
print("Mjenjac:")
print(f"Automatski: {amrm.get(0, 0)}")
print(f"Rucni: {amrm.get(1, 0)}")

#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
print("Automatski preko 100ks: ")
a100 = mtcars[(mtcars.am==0) & (mtcars.hp>100) & (mtcars.cyl==4)]
print(len(a100))

#7. Kolika je masa svakog automobila u kilogramima?
mtcars['masa_kg'] = mtcars['wt'] * 1000 * 0.453592
total_masa = mtcars['masa_kg'].sum()
print("Ukupna masa svih automobila: {total_masa:.2f} kg")
print("Masa svakog automobila u kg:")
print(mtcars[['car','masa_kg']])


