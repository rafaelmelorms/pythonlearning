#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Tuplas
'''Uma tupla é um outro contentor útil. É um tipo de dados para sequências ordenadas imutáveis de elementos. Elas são 
frequentemente usadas para armazenar pedaços relacionados de informação. Considere este exemplo envolvendo 
latitude e longitude:'''

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
'''Tuplas são semelhantes a listas, pois também armazenam uma coleção ordenada de objetos que podem ser acessados por meio
de seus índices. Ao contrário das listas, no entanto, as tuplas são imutáveis - não é possível adicionar e remover 
itens de tuplas ou classificá-las no lugar.'''

#As tuplas também podem ser usadas para fazer a atribuição de diversas variáveis de uma forma compacta.

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
#Os parênteses são opcionais ao definir tuplas, e programadores frequentemente os omitem caso não ajudem a esclarecer o código.

'''Na segunda linha, três variáveis são atribuídas a partir do conteúdo das dimensões tupla. Esse processo é chamado 
desempacotamento de tupla. Você pode usar o desempacotamento de tupla para atribuir as informações de uma tupla a 
múltiplas variáveis sem precisar acessá-las uma a uma e executar várias instruções de atribuição.'''

'''Se não precisássemos usar dimensions diretamente, poderíamos encurtar essas duas linhas de código para uma única linha que
atribui três variáveis de uma só vez!'''

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))