#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Conjuntos
'''Um conjunto é um tipo de dados para coleções mutáveis não ordenadas de elementos únicos. Uma aplicação de um conjunto
é remover rapidamente duplicatas de uma lista.'''
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

#RESULTADO: {1, 2, 3, 6}


'''Conjuntos aceitam o operador in da mesma forma que as listas. Você pode adicionar elementos aos conjuntos usando o método 
add, e removê-los usando o método pop, tal como nas listas. Porém, quando você utiliza pop para remover um elemento de um 
conjunto, um elemento aleatório é removido. Lembre-se de que conjuntos, ao contrário das listas, não são ordenados, então, 
não há um “último elemento”.'''
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element
#False

fruit.add("watermelon")  # add an element
print(fruit)
#{'orange', 'apple', 'banana', 'watermelon', 'grapefruit'}

print(fruit.pop())  # remove a random element
#orange
print(fruit)
#{'apple', 'banana', 'watermelon', 'grapefruit'}

'''Outras operações que você pode executar com conjuntos incluem aquelas de conjuntos matemáticos. Métodos como união, interseção
e diferença são fáceis de realizar com conjuntos e são muito mais rápidos do que esses operadores com outros contentores.'''

