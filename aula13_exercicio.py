#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Quiz: Defina um dicionário
#Defina um dicionário chamado population, que contém estes dados:
'''
 Defina um dicionario chamado population,
 que contenha informação sobre as maiores
 cidades do mundo.
 A chave deve ser o nome da cidade (string)
 e seu valor a respectiva população em
 milhões de pessoas, conforme tabela abaixo:
'''
#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {
    "Shanghai" : 17.8,
    "Istanbul" : 13.3,
    "Karachi"  : 13.0,
    "Mumbai"   : 12.5
}

#population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

print(population)
#{'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

#QUESTION 2 OF 5
'''Qual dessas poderia ser usada como a chave para um dicionário (marque todas as alternativas corretas)? Dica: chaves de 
dicionário devem ser imutáveis, ou seja, devem ser de um tipo que não é alterável.'''

# (x) str
# (x) list
# ( ) int
# (x) float

#QUESTION 3 OF 5
'''O que acontece se procurarmos um valor que não está no dicionário? Em seu próprio computador, crie um dicionário de teste e 
use colchetes para pesquisar um valor ainda não definido. O que acontece?'''

#Ocorre um KeyError. Seria legal se o Python pudesse pesquisar na Internet para responder a qualquer pergunta, mas, se o Python 
#fosse tão inteligente, o mundo não precisaria de programadores! As outras duas opções são possíveis com um pouco mais de
#programação, mas não são como os dicionários funcionam por conta própria.

#get com um valor padrão
'''Os dicionários têm um método relacionado que também é útil, get. get procura por valores em um dicionário, mas, ao contrário 
de colchetes, devolve none (ou um valor padrão à sua escolha) se a chave não for encontrada. Se você espera que as pesquisas às 
vezes falhem, get pode ser uma ferramenta melhor do que as pesquisas normais com colchetes.'''

elements.get('dilithium')
#None
elements['dilithium']
#KeyError: 'dilithium'
elements.get('kryptonite', 'There\'s no such element!')
#"There's no such element!"
'''No último exemplo, especificamos um valor padrão (a string 'There\'s no such element!') a ser retornado em vez de None, quando 
a chave não for encontrada.'''

#Verificando igualdade x identidade: == vs. is

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
# True True True False

'''Isso está correto! Lista a e lista b são iguais e idênticas. A listacé igual aa(ebnesse caso já que elas têm o mesmo conteúdo). 
Masaec(eb`, nesse caso) apontam para dois objetos diferentes, ou seja, eles não são objetos idênticos. Essa é a diferença entre 
verificar igualdade e identidade.'''

#Contexto
'''Use o dicionário abaixo responder a TODAS as questões relacionadas a dicionários. Considere que você tenha um dicionário chamado 
animals, parecido com este abaixo:'''

animals = {
    'dogs': [20, 10, 15, 8, 32, 15], 
    'cats': [3,4,2,8,2,4], 
    'rabbits': [2, 3, 3], 
    'fish': [0.3, 0.5, 0.8, 0.3, 1]
    }

#O tipo de dados das chaves no dicionário.      STRING

#O tipo de dados dos valores no dicionário.     LIST

#O resultado de animals['dogs'].                [20, 10, 15, 8, 32, 15]

#O resultado de animals['dogs'][3].             8

#O resultado de animals[3]                      KeyError: 3

#O resultado de animals['fish']                 [0.3, 0.5, 0.8, 0.3, 1]

