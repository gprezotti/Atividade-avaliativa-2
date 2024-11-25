'''
Crie um conjunto de dados simulando uma relação linear: y=2x+3+ruído,
onde x varia de 0 a 10 (20 pontos). Use a álgebra matricial do NumPy para
calcular os coeficientes da regressão linear y=ax+b. Compare os resultados
com os obtidos usando a função numpy.polyfit.

Utilizarei o método dos mínimos quadrados para encontrar os valores dos coeficientes de regressão linear

np.vstack(tup, dtype, casting)
  tup -> sequência de arrays (precisam ter o mesmo shape)
  
@ -> Utilizado para multiplicação matricial
'''
import numpy as np

x = np.array(np.random.rand(20)) * 10
ruido = np.array(np.random.random(20)) * 10
y = 2*x + 3 + ruido

X = np.vstack([x, np.ones(len(x))]).T
coeficientes = np.linalg.inv(X.T @ X) @ X.T @ y

a, b = coeficientes
print(f"Alpha = {a}")
print(f"B = {b}")


print(f"\nUsabdo np.polyfit:")
print(np.polyfit(x, y, 1))