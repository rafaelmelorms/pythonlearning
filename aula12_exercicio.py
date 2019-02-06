#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#QUESTION 1 OF 3
#Qual seria a saída do seguinte código
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

#Resposta: 6

#QUESTION 2 OF 3
#Considere o seguinte código:

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

print(b)
#Depois de executar este código, será que o número 5 fará parte do conjunto b?
'''Resposta: Acertou. Quando você remove um elemento de um conjunto, um elemento aleatório é removido (lembre-se de que conjuntos, 
ao contrário das listas, não são ordenados, então, não há um “último elemento”). O número 5 pode ser ou não removido.'''
