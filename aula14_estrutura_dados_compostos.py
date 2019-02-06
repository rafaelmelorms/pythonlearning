#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Estruturas De Dados Compostas
'''Podemos incluir contentores em outros contentores para criar estruturas de dados compostas. Por exemplo, este dicionário
mapeia chaves para valores que são também dicionários!'''

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

# Podemos acessar elementos no dicionário aninhados assim.

helium = elements["helium"]  # pega o dicionário de helium
hydrogen_weight = elements["hydrogen"]["weight"]  # pega o weight (peso) de hydr

#Você também pode adicionar uma nova chave ao dicionário de elementos.
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # cria um novo dicionário oxygen
elements["oxygen"] = oxygen  # coloca 'oxygen' como chave para o dicionário de elementos 
print('elements = ', elements)

#O resultado é:
#elements =  {"hydrogen": {"number": 1,
#                          "weight": 1.00794,
#                          "symbol": 'H'},
#               "helium": {"number": 2,
#                         "weight": 4.002602,
#                         "symbol": "He"}, 
#              "oxygen": {"number": 8, 
#                         "weight": 15.999, 
#                         "symbol": "O"}}

