#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Quiz: Qual é o tipo destes objetos?
'''
QUESTION 1 OF 5
Qual é o tipo deste objeto? "12". Há um ambiente de programação, mais abaixo nesta página, que você pode utilizar para 
experimentação. Entre com seu código e o execute com o botão "Execução de teste".
'''
#str

'''
QUESTION 2 OF 5
Qual é o tipo deste objeto? 12.3 Tem um ambiente de programação, mais abaixo nesta página, que você pode usar para experimentação.
Entre com seu código e o execute com o botão "Execução de teste".
'''
#float

'''
QUESTION 3 OF 5
Qual é o tipo desse objeto? len("my_string") Tem um ambiente de programação, mais abaixo nesta página, que você pode usar para 
experimentação. Entre com seu código e o execute com o botão "Execução de teste".
'''
#int

'''
QUESTION 4 OF 5
Qual é o tipo desse objeto? "hippo" *12 Tem um ambiente de programação, mais abaixo nesta página, que você pode usar para experimentação. 
Entre com seu código e o execute com o botão "Execução de teste".
'''
#str
print(type("hippo" *12))
print("hippo" *12)

'''
Quiz: Vendas totais
Neste quiz, você precisará alterar os tipos dos dados de entrada e de saída a fim de obter o resultado desejado.

Calcule e exiba o total de vendas da semana a partir dos dados fornecidos. Exiba uma string da forma "This week's total 
sales: xxx", onde xxx será o total real de todos os números. Você precisará alterar os tipos de dados de entrada a 
fim de calcular o total.
'''
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

total = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales:", total)

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convertemos para String novamente!!
print("This week's total sales: " + weekly_sales)

#TODO: Imprima(Print) uma String no formato: This week's total sales: xxx
# É provável que você precise escrever algumas linhas de código antes do prin