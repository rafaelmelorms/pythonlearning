#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Listas!
'''
Você viu aqui que pode criar uma lista com colchetes. As listas podem conter qualquer mistura e combinação de tipos de dados
que você viu até agora.'''
lst_of_random_things = [1, 3.4, 'a string', True]

'''
Esta é uma lista de 4 elementos. Todos os contentores ordenados (como listas) são indexadas em Python usando um índice inicial 
de 0. Portanto, para puxar o primeiro valor da lista acima, podemos escrever:'''
lst_of_random_things[0]
#1

'''E se tentarmos obter o último elemento da lista com o código a seguir?'''
list_of_random_things[len(list_of_random_things)]
# IndexError Traceback (most recent call last) <ipython-input-34-f88b03e5c60e> in <module>() ----> 1 lst[len(lst)] IndexError: list index out of range

'''
Não funcionou pois estamos acessando um elemento que não existe (a posição dos elementos na lista começa pelo 0, enquanto a 
contagem realizada pela função len() começa por 1). No entanto, podemos obter o último elemento subtraindo 1 do índice. Então, 
podemos fazer o seguinte:'''
list_of_random_things[len(list_of_random_things) - 1]
#True

'''
Alternativamente, você pode indexar a partir do final de uma lista usando valores negativos, onde -1 é o último elemento, -2 é 
o penúltimo elemento e assim por diante.'''

list_of_random_things[-1]
#True

list_of_random_things[-2] 
#a string

#Cortando em pedaços menores com listas
'''
Você viu que conseguimos puxar mais de um valor por vez de uma lista se a cortarmos em pedaços menores. Ao usar o corte, é 
importante lembrar que o índice inferior é inclusivo e o índice superior é exclusivo.
'''
#Portanto:

list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[1:2]
#[3.4]

'''Devolve apenas 3,4 de uma lista. Observe que isto ainda é diferente do que indexar apenas um único elemento, pois você obterá 
uma lista com essa indexação. Os dois pontos dizem-nos para partir do valor à esquerda até, mas não incluindo, o 
elemento à direita.'''

#Se você sabe que você quer começar do início da lista, pode deixar esse valor em branco.

list_of_random_things[:2]
#[1, 3.4]
#ou, para puxar todos os elementos do final da lista, podemos deixar em branco o elemento final.

list_of_random_things[1:]
#[3.4, 'a string', True]
#Esse tipo de indexação funciona exatamente da mesma maneira com strings, onde o valor devolvido será uma string.

#Você está in OU not in?
'''Você viu que nós também podemos usar in e not in para retornar um bool que afirma se um elemento existe ou não dentro de nossa 
lista ou se uma string é uma substring de outra.'''

'this' in 'this is a string'
#True
'in' in 'this is a string'
#True
'isa' in 'this is a string'
#False
5 not in [1, 2, 3, 4, 6]
#True
5 in [1, 2, 3, 4, 6]
#False

#Mutabilidade e ordem
'''Mutabilidade indica se podemos ou não alterar um objeto depois que ele foi criado. Se um objeto (como uma lista ou string) pode 
ser alterado (tal qual uma lista pode), então dizemos que ele é mutável. No entanto, se um objeto não pode ser alterado com a 
criação de um objeto completamente novo (como as strings), então o objeto é considerado imutável.'''
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
#['one', 2, 3, 4, 5]

#Como mostrado acima, você é capaz de substituir 1 por 'um' na lista acima. Isso ocorre porque listas são mutáveis.
#No entanto, o seguinte não funciona:
greeting = "Hello there"
greeting[0] = 'M'

'''Isso ocorre porque strings são imutáveis Isso significa que, para alterar uma string, você precisará criar uma string completamente
nova.
Há duas coisas a se ter em mente para cada um dos tipos de dados que você está usando:
1. Eles são mutáveis?
2. Eles são ordenados?
Tanto strings quanto listas são ordenadas. No entanto, nas próximas seções, você verá alguns tipos de dados que não serão 
ordenados. Para cada uma das próximas estruturas de dados que você verá, é útil entender como você deve indexar, se 
são mutáveis e se são ordenados. Saber isso sobre a estrutura de dados é realmente útil!'''

#Além disso, você verá como cada um deles tem métodos diferentes, então, utilizar uma estrutura de dados ou outra é 
#largamente dependente dessas propriedades, e o que você pode facilmente fazer com elas!
