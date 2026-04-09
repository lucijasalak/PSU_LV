import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# Definicija stvarne funkcije
def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

# Funkcija za dodavanje šuma
def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

# Generiramo podatke
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# Podjela na trenirajući i testni skup
np.random.seed(12)
indeksi = np.random.permutation(len(x))
indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]
indeksi_test = indeksi[int(np.floor(0.7*len(x)))+1:len(x)]

xtrain = x[indeksi_train]
ytrain = y_measured[indeksi_train]

xtest = x[indeksi_test]
ytest = y_measured[indeksi_test]

# Stvaramo polinomske značajke za različite stupnjeve
degrees = [2, 6, 15]
MSEtrain = []
MSEtest = []

plt.figure(figsize=(12, 8))

for degree in degrees:
    # Kreiraj polinomske značajke za trenutni stupanj
    poly = PolynomialFeatures(degree=degree)
    xnew_train = poly.fit_transform(xtrain)
    xnew_test = poly.transform(xtest)
    
    # Kreiraj linearni model
    linearModel = lm.LinearRegression()
    linearModel.fit(xnew_train, ytrain)
    
    # Predviđanje za trenirajući i testni skup
    ytrain_p = linearModel.predict(xnew_train)
    ytest_p = linearModel.predict(xnew_test)
    
    # Izračunaj MSE
    MSEtrain.append(mean_squared_error(ytrain, ytrain_p))
    MSEtest.append(mean_squared_error(ytest, ytest_p))
    
    # Grafički prikaz modela
    plt.subplot(3, 1, degrees.index(degree) + 1)
    plt.plot(x, y_true, label='True Function', color='black')
    plt.plot(xtrain, ytrain_p, label=f'Model (degree={degree})', linestyle='--')
    plt.scatter(xtrain, ytrain, color='blue', label='Train Data')
    plt.scatter(xtest, ytest, color='red', label='Test Data')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Polynomial Model with degree={degree}')

# Prikaz svih slika
plt.tight_layout()
plt.show()

# Ispis MSE za treniranje i testiranje
print("MSE za treniranje:", MSEtrain)
print("MSE za testiranje:", MSEtest)

# Simulacija s različitim brojem uzoraka za učenje (manji broj uzoraka)
x_small = np.linspace(1,10,20)
y_true_small = non_func(x_small)
y_measured_small = add_noise(y_true_small)
x_small = x_small[:, np.newaxis]
y_measured_small = y_measured_small[:, np.newaxis]

xtrain_small = x_small[:int(np.floor(0.7*len(x_small)))]
ytrain_small = y_measured_small[:int(np.floor(0.7*len(x_small)))]
xtest_small = x_small[int(np.floor(0.7*len(x_small))):]
ytest_small = y_measured_small[int(np.floor(0.7*len(x_small))):]

MSEtrain_small = []
MSEtest_small = []

for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
    xnew_train_small = poly.fit_transform(xtrain_small)
    xnew_test_small = poly.transform(xtest_small)
    
    linearModel = lm.LinearRegression()
    linearModel.fit(xnew_train_small, ytrain_small)
    
    ytrain_p_small = linearModel.predict(xnew_train_small)
    ytest_p_small = linearModel.predict(xnew_test_small)
    
    MSEtrain_small.append(mean_squared_error(ytrain_small, ytrain_p_small))
    MSEtest_small.append(mean_squared_error(ytest_small, ytest_p_small))

print("\nSimulacija s manjim brojem uzoraka:")
print("MSE za treniranje (manji broj uzoraka):", MSEtrain_small)
print("MSE za testiranje (manji broj uzoraka):", MSEtest_small)
