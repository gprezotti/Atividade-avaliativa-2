'''
Crie um array com os valores x=[0,π/2,π,3π/2,2π]. Calcule o seno e o
cosseno de cada valor.
'''
import numpy as np

radianos = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], dtype=float)

for i in range(len(radianos)):
  print(f"Seno de {radianos[i]} = {np.sin(radianos[i])}")
  print(f"Cosseno de {radianos[i]} = {np.sin(radianos[i])}\n")