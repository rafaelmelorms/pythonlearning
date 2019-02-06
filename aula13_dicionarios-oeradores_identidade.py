#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Dicionários E Operadores De Identidade
#Dicionários
'''Um dicionário é um tipo de dado mutável que armazena mapeamentos de chaves exclusivas para os valores. Aqui está um 
dicionário que armazena elementos e seus números atômicos.'''

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

'''Os dicionários podem ter chaves de qualquer tipo imutável, como inteiros ou tuplas, não apenas strings. Não é necessário 
sequer que todas as chaves sejam do mesmo tipo! Podemos procurar por valores ou inserir novos valores no dicionário usando 
colchetes que contenham a chave.'''

print(elements["helium"])  # imprime o valor mapeado a "helium"
elements["lithium"] = 3  # insere "lithium" com um valor de 3 no dicionário

'''Podemos verificar se um valor está em um dicionário da mesma forma que verificamos se um valor está em uma lista ou conjunto 
com a palavra-chave in. Os dicionários têm um método relacionado que também é útil, o get. Esse método procura valores em um 
dicionário, mas, ao contrário de colchetes, devolve none (ou um valor padrão de sua escolha) se a chave não for encontrada.'''

print("carbon" in elements)
print(elements.get("dilithium"))
#O que resultaria na saída:

# True
# None

'''Carbono está no dicionário, então True é exibido. Dilithium não está em nosso dicionário, então none é devolvido por get e 
depois exibido. Se você espera que as pesquisas às vezes falhem, get pode ser uma ferramenta melhor do que as pesquisas normais 
com colchetes, porque erros podem quebrar o seu programa.'''

#Operadores de identidade
#Keyword	Operator
#is     	avalia se ambos os lados têm a mesma identidade
#is not 	avalia se ambos os lados têm identidades diferentes

'''Você pode verificar se uma chave devolveu none com o operador is. Você pode verificar o oposto utilizando is not.'''

n = elements.get("dilithium")
print(n is None)
print(n is not None)
#O que resultaria na saída:

#True
#False