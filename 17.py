'''
Crie uma matriz quadrada 3×3 aleatória. Calcule o determinante e, se
possível, a inversa dessa matriz.
'''
import numpy as np

matriz = np.array([np.random.randint(0, 11, 3), np.random.randint(0, 11, 3), np.random.randint(0, 11, 3)], dtype=int)
print(matriz)
print(f"\nDeterminante = {np.linalg.det(matriz):.2f}")
print(f"\nMatriz Inversa:")
print(np.linalg.inv(matriz))