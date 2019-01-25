#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
O realce de cor também é uma indicação do erro ocorrido na string, nesse segundo caso. 
Há uma variedade de outras operações que você também pode utilizar com strings. Neste vídeo, você viu algumas:
'''

first_word = 'Hello'
second_word = 'There'
print(first_word + second_word)
#HelloThere

print(first_word + ' ' + second_word)
#Hello There

print(first_word * 5)
#HelloHelloHelloHelloHello

print(len(first_word))
#5

'''
Diferentemente de outros tipos de dados que tenha visto até agora, você também pode indexar strings, mas 
veremos mais sobre isso em breve! Por enquanto, aqui está um pequeno exemplo: Veja que o Python 
usa o índice 0 - nós discutiremos isso em detalhes mais tarde nesta aula.
'''
first_word[0]
#H

first_word[1]
#e

'''
A função len()
'len()' é uma função interna do Python que retorna o comprimento de um objeto, como uma string. O comprimento de uma 
string é o número de caracteres na string. Sempre será um número inteiro.
'''
#Há um exemplo acima, mas segue outro:

print(len("ababa") / len("ab"))
#2.5
'''
Você sabe quais são os tipos de dados para len("ababa") e len("ab"). Observe o tipo de dados do 
quociente resultante aqui.
'''
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"


name_length = len(given_name) + len(middle_names) + len(family_name) + 3
print(name_length)

print(len("rafa"))
