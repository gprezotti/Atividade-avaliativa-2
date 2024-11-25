'''
Simule um conjunto de dados com 50 amostras (linhas) e 3 características
(colunas) usando números aleatórios entre 0 e 1. Para cada coluna, calcule:
a. A média e o desvio padrão.
b. O valor máximo e o valor mínimo.
c. Normalize os dados de cada coluna para que fiquem no intervalo [0, 1].

np.man/min(a, axis, out, keepdims, initial, where)
np.std(a, axis, dtype, out, ddof, keppdims, where)
np.mean(a, axis, dtype, out, keepdims, where)
  a -> Array contendo números
  axis -> Eixo ao longo dos quais as médias são computadas
          axis=0 -> A operação é realizada ao longo das linhas. O cálculo ocorre em colunas
          axis=1 -> A operação é realizada ao longo das colunas. O cálculo ocorre em linhas
  dtype -> Tipo a ser usdo (por padrão "float64")
  
np.random.random(size)
  size = Int. Quantidade de números aleatórios dentro no intervalo [0, 1] a serem formados.
'''
import numpy as np

array = np.random.random((50, 3))
print(array)

media = np.mean(array, axis=0)
print(f"\nMédia de cada coluna: {media}")

desvioPadrao = np.std(array, axis=0)
print(f"\nDesvio padrão de cada coluna: {desvioPadrao}")

valorMax = np.max(array, axis=0)
print(f"\nValor máximo por coluna: {valorMax}")

valorMin = np.min(array, axis=0)
print(f"\nValor mínimo por coluna: {valorMin}")

# OS DADOS JÁ ESTÃO NO INTERVALO [0, 1]. PORÉM, SEGUE CÓDIGO ABAIXO PARA NORMALIZAÇÃO:
dadosNormalizados = (array - np.min(array)) / (np.max(array) - np.min(array))
print(f"\nDados normalizados:")
print(dadosNormalizados)