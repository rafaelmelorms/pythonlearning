#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#Métodos de string
#Neste vídeo ,você foi introduzido aos métodos. Métodos são como algumas funções que já vimos:

len("this")
type(12)
print("Hello world")
'''
As três expressões acima são funções. Observe que usam parênteses e aceitam um argumento.

As funções type e print podem receber strings, floats, ints e muitos outros tipos de dados como argumentos e a função len 
também pode aceitar diferentes tipos de dados como argumentos, que você verá mais adiante nesta aula.

Um método em Python é semelhante a uma função, mas atua em uma variável que você já criou. Métodos são específicos 
para o tipo de dado que é armazenado em uma variável particular.

Abaixo está uma imagem que mostra os métodos que são possíveis para qualquer string.
'''

#Cada um desses métodos aceita a string em si como seu primeiro argumento. No entanto, eles também podem receber argumentos 
# adicionais. Vamos olhar a saída para alguns exemplos.
my_string.islower()
#True
my_string.count('a')
#2
my_string.find('a')
#3
'''
Você pode ver que ambos os métodos count e find podem aceitar outro argumento. No entanto, o método islower não aceita um 
argumento. Se fôssemos armazenar um float, int ou outro tipo de dado em uma variável, os métodos disponíveis seriam completamente 
diferentes!

Nenhum profissional decora todos os métodos, por isso é tão importante entender como usar a documentação e encontrar respostas. 
Obter uma forte compreensão dos fundamentos de programação permitirá que você use essas bases para utilizar a documentação 
para construir muito mais do que alguém que tenta memorizar todas as funções disponíveis no Python.

Um método string importante: format()
Utilizaremos bastante o método de string format() em nosso futuro trabalho no Python, e você descobrirá que esse método é 
muito valioso durante a programação, especialmente com as declarações print.
'''
#Podemos melhor ilustrar como utilizar o format() ao observar alguns exemplos:

# Examplo 1
print("Mohammed has {} balloons".format(27))
Mohammed has 27 balloons
# Examplo 2
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
Does your dog bite?
# Examplo 3
maria_string = "Maria loves {} and {}"
print(maria_string.format("math","statistics"))
Maria loves math and statistics

#Em cada exemplo, observe como o número de chaves {} utilizado dentro da string é o mesmo número de substituições que se deseja 
##fazer usando os valores dentro de format().

#Os alunos com conhecimentos mais avançados podem aprender mais sobre a sintaxe formal para utilização do método de string 
#format() aqui.

# https://docs.python.org/3.6/library/string.html#format-string-syntax
# https://docs.python.org/3/library/stdtypes.html#string-methods
animal = "dog"
action = "come"
print(str.capitalize("rafael MELO sAnToS"))
print(str.isnumeric("1234"))
print(str.isnumeric("Rafael"))

print("Meu {} {} ração".format(animal, action))

#Outro importante método de string: split()
'''
Um método de string útil ao trabalhar com strings é o método .split. Esta função ou método retorna um contêiner de dados, 
denominado como uma lista que contém as palavras da string de entrada. Apresentaremos o conceito de listas no próximo vídeo.

O método split tem dois argumentos adicionais (sep e maxsplit). O argumento sep significa "separador". Ele pode ser usado 
para identificar como a string deve ser dividida (por exemplo, caracteres de espaço em branco como espaço, tabulação, enter, 
nova linha; pontuação específica, por exemplo, vírgula, traços). Se o argumento sep não for definido, por padrão, o separador 
será o espaço em branco.

Conforme o seu nome, o argumento maxsplit fornece o número máximo de divisões. O argumento maxsplit + 1 fornece o número de 
elementos na nova lista, com a string restante sendo retornada como o último elemento na lista. Você também pode saber mais 
sobre esses métodos na documentação do Python.
'''
#Aqui estão alguns exemplos do método .split() .
#01 - Um método básico da função split:
new_str = "The cow jumped over the moon."
new_str.split()
#O resultado é:
#['The', 'cow', 'jumped', 'over', 'the', 'moon.']

#02 - Abaixo, o separador é o espaço, e o argumento maxsplit é definido como 3.
new_str.split(' ', 3)
#O resultado é:
#['The', 'cow', 'jumped', 'over the moon.']

#02 - Usando '.' ou ponto como um separador.
new_str.split('.')
#O resultado é:
#['The cow jumped over the moon', '']

#03 - Não utilizando separadores, mas tendo um argumento maxsplit de 3.
new_str.split(None, 3)
#O resultado é:
#['The', 'cow', 'jumped', 'over the moon.']