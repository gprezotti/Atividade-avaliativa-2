'''
Crie um array de números de 0 a 50. Extraia os elementos pares e os
múltiplos de 5 desse array.
'''
import numpy as np

array = np.array(np.arange(0, 51))
pares = []
multiplos5 = []

pares.append(array[array % 2 == 0])
multiplos5.append(array[array % 5 == 0])
print(np.union1d(pares, multiplos5))