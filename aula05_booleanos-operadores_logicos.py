#!/usr/bin/python3.6
# -*- coding: utf-8 -*-


#Booleanos, operadores de comparação e operadores lógicos
'''
O tipo de dados bool contém os valores True ou False que, geralmente, são codificados como 1 ou 0, respectivamente.
Existem seis operadores de comparação que são comuns para obter um valor bool:
Operadores de comparação
Caso de uso de símbolo	Bool	Operação
5 < 3	                False	Menor do que
5 > 3	                True	Maior do que
3 <= 3	                True	Menor do que ou igual a
3 >= 5	                False	Maior do que ou igual a
3 == 5	                False	Igual a
3 != 5	                True	Não é igual a
E existem três operadores lógicos com que você precisa ter familiaridade:
Uso de lógica	    Bool	Operação 
5 < 3 and 5 == 5	False	and - Avalia se ambas as declarações fornecidas são verdadeiras
5 < 3 or 5 == 5	    True	or - Avalia se pelo menos uma das declarações fornecidas é verdadeira
not 5 < 3	        True	not - Inverte o valor bool
'''

age = 14
teen = not age > 12 and age < 18
print(teen)

age = 14
is_teen = age > 12 and age < 18
print(is_teen)

#QUIZ
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Escreva um código que imprima na tela (print) True se 
#  San Francisco for mais densa que Rio e False caso contrário

population = san_francisco_pop_density > rio_de_janeiro_pop_density
print(population)

#Ou

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)