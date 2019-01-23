#!/usr/bin/python
# -*- coding: utf-8 -*-
#PORCENTAGEM
# Volume atual de um reservatório de água (em metros cúbicos)
reservoir_volume = 4.445e8
reservoir_volume2 = 4.445 * 10 ** 8

# Total de água da chuva de uma tempestade(em metros cúbicos)
rainfall = 5e6
rainfall2 = 5 * 10 ** 6
rainfall *= .9

# Reduza a variável de água da chuva(rainfall) em 10% para considerar perdas
perda = (rainfall2 - (rainfall2 * 10 /100))
reservoir_volume += rainfall

# Adicione a variável rainfall à variaável de vol. atual do reservatório(reservoir_volume)
total_reservoir = perda + reservoir_volume2
reservoir_volume *= 1.05

# aumente o volume do reservatório (reservoir_volume) em 5% para considerar águas tempestuosas
# que chegam no reservatório dias apoós a tempestade
aumento = (total_reservoir + (total_reservoir * 5 / 100))
reservoir_volume *= 0.95

# reduza o volume do reservatório (reservoir_volume) em 5% para considerar evaporaçaão 
reducao = (aumento - (aumento * 5 / 100))
print(reducao)
reservoir_volume *= 0.95

# Subtraia 2.5e5 metros cúbicos de reservoir_volume para considerar água
# que édirecionada para regiões áridas.
newvolume = 2.5 * 10 ** 5
print(newvolume)
total = reducao - newvolume
reservoir_volume -= 2.5e5 

# execute um print do novo valor de reservoir_volume
print(total)
print(reservoir_volume)

teste = 5e6 
teste = teste * .9
print(teste) 

rainfall = 5e6
teste2 = (rainfall -(rainfall * 10 / 100))
print(teste2)
