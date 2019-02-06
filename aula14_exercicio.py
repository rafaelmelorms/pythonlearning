#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Quiz: Adicionando valores a dicionários aninhados
'''Experimente trabalhar com dicionários aninhados. Adicione uma outra entrada, 'is_noble_gas', para cada dicionário no dicionário 
elements. Depois de inserir as novas entradas, você deve ser capaz de executar estas pesquisas:'''
'''
>>> print(elements['hydrogen']['is_noble_gas'])
False
>>> print(elements['helium']['is_noble_gas'])
True
'''

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Adicione uma entrada 'is_noble_gas' para hydrogen e helium identificando se são gases nobres
# dica: helium é um gás nobre, hydrogênio não
elements['hydrogen']['is_noble_gas']=False
elements['helium']['is_noble_gas']=True

print(elements['helium']['is_noble_gas'])
print(elements['hydrogen']['is_noble_gas'])


#Coleções
'''Quando temos um grupo de dados, podemos pensar nele como uma coleção (de elementos de dados). Nesta aula, vimos muitas 
estruturas de dados diferentes, que o Python fornece para armazenar, acessar e manipular coleções de dados. Em especial, 
listas, conjuntos e dicionários.'''

#Nos próximos quizzes, você terá a oportunidade de praticar e revisar as propriedades de listas, conjuntos e dicionários.

#QUESTION 2 OF 4
#Verifique os atributos de uma coleção na qual utilizar uma lista Python seria apropriado.
'''
( ) A ordem na qual você adiciona itens não importa.
(X) Os itens são sempre indexados com números, começando em 0
(X) Ordenáveis
(X) Adicionar itens com .append
( ) Adicionar itens com .add 
'''

#QUESTION 3 OF 4
#Verifique os atributos de uma coleção para a qual utilizar um conjunto Python seria apropriado.
'''
(X) A ordem em que os itens aparecem pode ser inconsistente
( ) Você pode ter a mesma entrada várias vezes.
(X) Mutável (que você pode alterar)
(X) Adicionar itens com .add
( ) Ordenáveis
'''

#QUESTION 4 OF 4
#Verifique os atributos de uma coleção para a qual utilizar um dicionário Python seria apropriado
'''
(X) Cada item contém duas partes
( ) Adicionar itens com .append
(X) A ordem em que os itens aparecem pode ser inconsistente
( ) Ordenáveis
(X) Podem ser aninhados
'''

#Exercícios para praticar
'''As perguntas a seguir foram baseadas no primeiro verso do poema If por Rudyard Kipling. Convertemos todas letras para minúsculas, 
removemos toda pontuação do texto e armazenamos o texto modificado na variável verse, do tipo string.'''

#Quiz: Conte palavras únicas
'''Sua tarefa para este quiz é encontrar o número de palavras únicas no texto. No editor de código abaixo, complete estes três passos 
para obter sua resposta.

1. Separe verse em uma lista de palavras.
2. Converta a lista para uma estrutura de dados capaz de armazenar apenas seus elementos únicos.
3. Exiba o comprimento do container escolhido no item 2.
'''
#Dica: Você pode usar um método de string visto nos tópicos anteriores.
verse = "if you can keep your head when all about you are losing theirs and blaming it on you if you can trust yourself when all men doubt you but make allowance for their doubting too   if you can wait and not be tired by waiting or being lied about  don’t deal in lies or being hated  don’t give way to hating and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

#Quiz: Dicionário de versos
'''No editor de código abaixo, você encontrará um dicionário contendo as palavras únicas de verse armazenadas como chaves e o 
número de vezes que elas apareceram em verse armazenadas como valores. Use este dicionário para responder as perguntas a 
seguir. Envie estas respostas no quiz abaixo do editor de código.'''
#Tente responder o quiz usando código, em vez de inspecionar o dicionário manualmente!

# 1. Quantas palavras únicas existem em verse_dict?
# 2. A chave "breathe" está contida em verse_dict?
# 3. Qual é o primeiro elemento da lista criada quando verse_dict é ordenado segundo suas chaves?
# 4. Qual é o último elemento da lista criada quando verse_dict é ordenado segundo suas chaves?
'''Dica: Use o método keys() para obter uma lista das chaves do dicionário, e então use o método apropriado para ordenar esta lista. 
Use esta lista ordenada de chaves para responder as perguntas 3 e 4.'''
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict.keys()))
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = ("breathe" in verse_dict)
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 





