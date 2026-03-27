
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka
mtcars = pd.read_csv("mtcars.csv")

# Dodaj 'car' stupac ako nije index
if 'car' not in mtcars.columns:
    mtcars['car'] = mtcars.index

# 1. Barplot - prosječna potrošnja po broju cilindara
avg_mpg = mtcars.groupby('cyl')['mpg'].mean()
plt.figure(figsize=(8,5))
plt.bar(avg_mpg.index.astype(str), avg_mpg.values, color=['skyblue', 'orange', 'green'])
plt.title("Prosječna potrošnja automobila po broju cilindara")
plt.xlabel("Broj cilindara")
plt.ylabel("Potrošnja (mpg)")
plt.show()

# 2. Boxplot - distribucija težine po broju cilindara
wt_data = [mtcars[mtcars['cyl']==c]['wt'] for c in sorted(mtcars['cyl'].unique())]
plt.figure(figsize=(8,5))
plt.boxplot(wt_data, labels=[str(c) for c in sorted(mtcars['cyl'].unique())])
plt.title("Distribucija težine automobila po broju cilindara")
plt.xlabel("Broj cilindara")
plt.ylabel("Težina (1000 lbs)")
plt.show()

# 3. Potrošnja vs mjenjač (ručni vs automatski)
mpg_am = [mtcars[mtcars['am']==i]['mpg'] for i in [0,1]]
plt.figure(figsize=(8,5))
plt.boxplot(mpg_am, labels=['Automatski','Ručni'])
plt.title("Potrošnja automobila: ručni vs automatski mjenjač")
plt.ylabel("Potrošnja (mpg)")
plt.show()

# 4. Odnos ubrzanja i snage po tipu mjenjača
plt.figure(figsize=(8,5))
plt.scatter(mtcars[mtcars['am']==0]['hp'], mtcars[mtcars['am']==0]['qsec'], color='red', label='Automatski')
plt.scatter(mtcars[mtcars['am']==1]['hp'], mtcars[mtcars['am']==1]['qsec'], color='blue', label='Ručni')
plt.title("Odnos ubrzanja (qsec) i snage (hp) po tipu mjenjača")
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Ubrzanje (qsec)")
plt.legend()
plt.show()