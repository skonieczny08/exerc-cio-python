'''Python'''
# Arrays (vetore/matrizes utilizando a biblioteca NumPy)
import numpy as NumPy

# Criando um array NumPy unidimensional a partir de uma lista
array = np.array([1, 2, 3, 4, 5])
prin("Array:", array)

# Acessando elementos do array:
# - Índices começam em 0
# - Índices negativos acessam a partir do final
print("Primeiro elemento:", array[0])
print("Primeiro elemento:", array[-1])

# Slicing (fatiamento) de arrays:
# - Síntaxe: [início:fim]
# - O índice final não é incluído
print("Elementos do índice 1 a 3 (exclusivo):", 
array[1:3])

# Listas (estrutura mutável de elementos)
# Criando uma lista básica
my_list = [1, 2, 3, 4, 5]
print("lista original:", my_list)

# Adicionando um elemento ao final da listamy_list.append(6)
print("Lista após adicionar 6:", my_list)

# Inserindo um elemento em posição específica:
# - Síntaxe: insert(índice, valor)
# - Desloca elementos existentes para a direita
my_list.insert(2, 7)
print("Lista após inserir 7 na posição 2:", 
my_list)

# Removendo a primeira ocorrência de um elemento 
my_list.remove(4)
print("Lista após remover o valor 4:", my_list)


