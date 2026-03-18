
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"),
                  usecols=(1,2,3,4,5,6),
                  delimiter=",",
                  skiprows=1)

mpg=data[:,0]
cyl=data[:,1]
disp=data[:,2]
hp=data[:,3]
drat=data[:,4]
wt=data[:,5]


plt.scatter(hp, mpg, s=wt*20)
plt.xlabel("konjske snage(hp)")
plt.ylabel("potrosnja(mpg)")
plt.title("ovisnost hp o mpg")
plt.show()

mpg_min = np.min(mpg)
mpg_maks = np.max(mpg)
suma = np.sum(mpg)
broj = len(mpg)
prosjek = suma / broj

print("mpg minimum:", mpg_min)
print("mpg maksimum:", mpg_maks)
print ("mpg prosjek: ", prosjek)

mpg6 = mpg[cyl ==6]
mpg_min6 = np.min(mpg6)
mpg_maks6 = np.max(mpg6)
suma = np.sum(mpg6)
broj = len(mpg6)
prosjek = suma / broj

print("mpg6 minimum:", mpg_min6)
print("mpg6 maksimum:", mpg_maks6)
print ("mpg6 prosjek: ", prosjek)

