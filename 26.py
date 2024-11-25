'''
Crie um array com 30 números inteiros aleatórios entre 0 e 10. Identifique os
valores únicos e conte a frequência de cada valor.

np.random.randint(low, high, size, dtype)
  low -> Int. Menor valor podendo ser mostrado
  high -> Int. Maior valor podendo ser mostrado (se desejar que o maior número a ser mostrado seja 'n', high deverá ser 'n+1')
  size -> Tamanho do array de número aleatórios a ser mostrado
  
np.unique(ar, return_index, return_inverse, return_counts, axis)
  ar -> Array de entrada
  return_index -> Bool. Se True, retorna o indice do 'ar' que resulta em um array único
  return_inverse -> Bool. Se True, retorna o indice do array único que pode ser usado para reconstuir 'ar'
  return_count -> Bool. Se True, retorna a quantidade de vezes que cada valor aparece no 'ar'
  axis -> Int. Eixo ao qual a operação será efetuada
    axis=0 -> A operação é realizada ao longo das linhas. A operação ocorre em colunas
    axis=1 -> A operação é realizada ao longo das colunas. A operação ocorre em linhas
'''
import numpy as np

array = np.array(np.random.randint(0, 11, 30), dtype=int)
valorUnicos, frequencia = np.unique(array, return_counts=True)

print(array)
print(f"\nArray único: {valorUnicos}")
print(f"Frequência dos números: {frequencia}")