#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
Quiz: Corrigir a citação
A linha de código no quiz a seguir causará um SyntaxError, graças à utilização indevida de 
aspas. Primeiro, faça uma execução de teste para ver a mensagem de erro. Em seguida, resolva 
o problema para que a citação (de Henry Ford) seja corretamente atribuída à variável ford_quote.
'''
# TODO: Arrume essa String!
ford_quote = 'Whether you think you can, or you think you can"t--you"re right.'
print(ford_quote)

# TODO: Corrija essa string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

# TODO: Corrija essa string!
ford_quote = "Whether you think you can, or you think you can't--you're right."


#QUESTION 2 OF 5
#Nós já vimos que o tipo de objetos afetará como os operadores funcionam. Qual será a saída deste código?
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

#3415  (e tropical_fruit_count é uma string)

'''
Quiz: Escreva uma mensagem de log no servidor
Neste quiz de programação, você vai usar o que aprendeu sobre strings para escrever uma mensagem de log para um servidor.
Forneceremos exemplos de dados de um usuário, com o tempo de sua visita e o site acessado. Você deve usar as 
variáveis fornecidas e as técnicas que aprendeu para imprimir uma mensagem de log como esta (com o nome de 
usuário, URL e marcação de tempo substituídos pelos valores das variáveis apropriadas):
Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.
Use o botão de execução de teste para ver os resultados enquanto você trabalha no código pedaço por pedaço.
'''
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: imprima(print) uma mensagem de log incorporando as Strings acima.
# A mensagem deve seguir o mesmo formato que:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username +' ' + 'accessed the site' +' ' + url + ' ' +'at' +' ' + timestamp + '.')
message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)


print (username + " accessed the site " + url + " at " + timestamp + ".")
#OU
message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)


'''
Quiz: len()
Utilize a concatenação de strings e a função len para encontrar o comprimento do nome completo de uma estrela de 
cinema real. Armazene esse comprimento na variável name_length. Não se esqueça de que existem espaços entre as 
diferentes partes de um nome!
'''
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name) + len(middle_names) + len(family_name) + 2

# Confirme se o nome tem o número de caracteres permitido na Carteira de Motorista
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

'''
QUESTION 5 OF 5
Acabamos de utilizar a função len para encontrar o comprimento de strings. O que a função de len devolve quando colocamos 
o inteiro 835, em vez de uma string?
'''
#Error