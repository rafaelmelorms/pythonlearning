#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Quiz: Indexação de lista
'''Use a indexação de lista para determinar quantos dias existem em um mês específico com base na variável month, de tipo inteiro,
e armazene esse valor na variável de tipo inteiro num_days. Por exemplo, se month for 8, num_days deve ser definida como 31, 
já que o oitavo mês, agosto, possui 31 dia'''

#Lembre-se de considerar que a indexação é baseada no zero!
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Use a indexação de lista para definir a variável num_days com quantos dias existem em um mês específico
num_days = days_in_month[7]
num_days2 = days_in_month[month - 1]
print(num_days)
print(num_days2)

#Quiz: Cortando listas
'''Selecione as três datas mais recentes desta lista usando a notação de corte de lista. Dica: índices negativos 
funcionam para as fatias!'''
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modifique essa linha para que imprima (print) os últimos 3 elementos da lista

print(eclipse_dates[-3:])

#QUESTION 3 OF 3
#Suponha que tenhamos as duas expressões seguintes, sentence1 e sentence2:
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
'''Relacione o código Python abaixo com o valor modificado de sentence1 ou sentence2. Se o código resultar em um erro, faça a 
correspondência com “Erro”.'''
#sentence1 é uma string e é, portanto, um objeto imutável. Isso significa que, por mais que você possa se referir a 
# caracteres individuais de sentence1 (por exemplo, você pode escrever coisas como sentence1[5]), não pode atribuir 
# valor para eles (você não pode escrever coisas como sentence1[5] = 'a'). Portanto, a terceira expressão resultará em erro.

#sentence2 é uma lista, e listas são mutáveis, significando que você pode alterar o valor de itens individuais em sentence2:

#Na primeira expressão, alteramos o valor do último item em sentence2 de "." para "!".
#Na segunda expressão, alteramos o valor do último item em sentence2 de "I" para "Our Majesty".
#Na última expressão, utilizamos cortes para alterar simultaneamente o valor do primeiro e do segundo item em sentence2 de "I" 
#e "wish" para "We" e "want"