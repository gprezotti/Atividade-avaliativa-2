'''
Crie dois arrays 1D de tamanho 5. Eleve cada elemento do primeiro array ao
quadrado e subtraia o correspondente elemento do segundo array.
'''
import numpy as np

array1 = np.array(np.random.randint(0, 11, 5))
array2 = np.array(np.random.randint(0, 11, 5))

print(f"Array 1: {array1}")
print(f"Array 1 ao quadrado: {array1 ** 2}")
print(f"Array 2: {array2}")
print(f"Array 1 ao quadrado, menos Array 2: {(array1 ** 2) - array2}")