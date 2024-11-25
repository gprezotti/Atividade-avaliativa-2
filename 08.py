'''
Crie uma matriz quadrada 3x3 aleatória e calcule seus autovalores e
autovetores.
'''
import numpy as np

matriz = np.array([np.random.randint(0, 11, 3), np.random.randint(0, 11, 3), np.random.randint(0, 11, 3)], dtype=int)
print("Matriz:")
print(matriz)

autovalores, autovetores = np.linalg.eig(matriz)

print("\nAutovalores:")
print(autovalores)

print("\nAutovetores:")
print(autovetores)