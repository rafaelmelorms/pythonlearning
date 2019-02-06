#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Correção: no vídeo acima, na marcação de tempo de 0:42, o código deve ser

print("scores: " + str(scores))
print("grades: " + str(grades))

#Funções úteis para listas I
len() #devolve quantos elementos existem em uma lista.
batch_sizes = [15, 6, 89, 34, 65, 35]
print(len(batch_sizes))

max() #devolve o maior elemento da lista. A maneira como é determinado o maior elemento de uma lista depende de quais 
#tipos de objetos estão presentes na lista. O elemento máximo em uma lista de números é o maior número. O elemento máximo 
# de uma lista de strings é o elemento que ocorreria por último caso a lista estivesse em ordem alfabética. Isso funciona
#  porque a função máximo é definida em termos do operador de comparação ‘maior do que’. A função máximo é indefinida para
# listas que contêm elementos de tipos diferentes, incomparáveis.
batch_sizes = [15, 6, 89, 34, 65, 35]
print(max(batch_sizes))

min() #devolve o menor elemento em uma lista. Mínimo é o oposto de máximo e retorna o menor elemento de uma lista.
batch_sizes = [15, 6, 89, 34, 65, 35]
print(min(batch_sizes))

sorted() #devolve uma cópia de uma lista, ordenada do menor para o maior, deixando a lista inalterada.
sizez = [15, 6, 89, 34, 65, 35]
print(sorted(sizez))
print(sorted(sizez, reverse=True))

#Funções úteis para listas II
#Método join
'''Join é um método de strings que recebe uma lista de strings como argumento e devolve uma string formada pelos elementos 
da lista unidos por um separador de strings.'''

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
#Saída: 
#fore
#aft
#starboard
#port

'''Neste exemplo, usamos a string "\n" como separador para que haja uma nova linha entre cada elemento. Podemos também 
utilizar outras strings como separadores com .join. Aqui, usamos um hífen.'''
name = "-".join(["García", "O'Kelly"])
print(name)
#Saída: García-O'Kelly

'''É importante lembrar de separar cada um dos itens da lista que você está unindo, usando uma vírgula (,). Esquecendo de fazer 
isso não vai provocar um erro, mas vai gerar resultados inesperados.'''

#Método append
'''Um método útil chamado append adiciona um elemento ao final de uma lista.'''
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

#Saída: ['a', 'b', 'c', 'd', 'z']

#Tente você mesmo!
'''No início do primeiro vídeo, você viu como o comportamento das variáveis que contêm objetos mutáveis e imutáveis é muito 
diferente e pode até ser surpreendente às vezes! Experimente, use as funções print e verifique seu trabalho onde você puder,
para ter a certeza de que seus programas monitoram corretamente seus dados. Enquanto você experimenta as listas, tente usar 
algumas das funções úteis acima.'''

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#QUESTION 2 OF 4
#Qual seria a saída do seguinte código (trate a vírgula na resposta de múltipla escolha como uma nova linha)?
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
# Albert & Ben & Carol & Donna

#QUESTION 3 OF 4
#Qual seria a saída do seguinte código (trate a vírgula na resposta de múltipla escolha como uma nova linha)?
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
#['Albert', 'Ben', 'Carol', 'Donna', 'Eugenia']







