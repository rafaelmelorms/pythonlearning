#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#QUESTION 1 OF 3
'''
O que acontece quando você usa um método de string, como islower, em um objeto float? 
Por exemplo, 13.37.islower
No quiz que está mais abaixo desta página, há um playground que você pode usar para experimentação.
'''
# Ocorre um erro.

'''
Você pode aprender mais sobre strings e métodos de string na documentação dos métodos de string.
Você descobrirá que a documentação é um dos recursos mais valiosos para escrever códigos, não somente quando se trata de strings ou de escrever códigos em Python! Lendo e pesquisando a documentação, você pode aprender sobre tipos de dados e funções internas, bem como a forma de utilizá-los.
Experimente agora! Procure alguns métodos de string (usando o link acima) e teste-os no quiz de programação abaixo (usando o botão de execução de teste).
'''
#Sugestões:
# navegue na lista completa de métodos de string em:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# e teste alguns aqui
print(str.capitalize("rafael MELO sAnToS"))
print(str.isnumeric("1234"))
print(str.isnumeric("Rafael"))

'''
Utilizando o espaço abaixo, pratique o uso do método format(). A intenção aqui é praticar, 
não há certo ou errado para esse exercício.
'''
# Escreva duas linhas de codigo abaixo, cada uma associando um valor a uma variavel 
animal = "dog"
action = "come"

# Agora escreva um print utilizando .format() para retornar uma sentenca e 
# os valores das duas variaveis
print("Meu {} {} ração".format(animal, action))

