#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

#LINK TOP
# https://www.programiz.com/python-programming/operators
'''
Variáveis I
Variáveis são usadas o tempo todo em Python! Aqui abaixo está o exemplo que você viu no vídeo, em que fizemos o seguinte:

mv_population = 74728

Aqui, mv_population é uma variável que contém o valor 74728. Isso atribui o 
item à direita ao nome à esquerda, o que é, na verdade,um pouco diferente da 
igualdade matemática, já que 74728 não armazena o valor de mv_population.

Em qualquer caso, independentemente de qual for o termo do lado esquerdo, 
ele agora é um nome para o valor que está do lado direito. Uma vez que um valor tiver sido atribuído a um nome de variável, 
você pode acessá-lo pelo nome da variável.
'''
#Exemplo 01
x = 2
y = x

print(y)

#Exemplo 02
x = 3
y = 4
z = 5
#ou 
x, y, z = 3, 4, 5

'''
No entanto, a maneira acima não é a melhor para atribuir variáveis, na maioria dos casos, porque nossos nomes de 
variáveis devem ser descritivos dos valores que detêm.

Além de escrever nomes de variáveis que sejam descritivos, há algumas coisas que devemos observar ao nomear variáveis em Python.

1. Utilize apenas letras comuns, números e sublinhados em seus nomes de variáveis. Eles não podem conter espaços e precisam 
começar com uma letra ou sublinhado.

2. Você não pode usar palavras reservadas ou identificadores internos que tenham finalidades importantes em Python, você vai 
aprender sobre elas durante todo o curso. Uma lista de palavras reservadas em Python está descrita aqui. Criar nomes que 
sejam descrições dos valores geralmente ajuda a evitar o uso dessas palavras. Uma pequena tabela de tais palavras também 
está disponível abaixo.
'''

#Palavras chaves no Python - Keywords in Python programming Language
'''
and	assert	break	class	continue
def	del	elif	else	except
exec	finally	for	from	global
if	import	in	is	lambda
not	or	pass	print	raise
return	try	while	
'''

#A maneira de nomear variáveis em Python é utilizar somente letras minúsculas e separar as palavras com sublinhados.
# Correto
my_height = 58
my_lat = 40
my_long = 105

#Errado
#my height = 58
#MYLONG = 40
#MyLat = 105

'''
Por mais que estas últimas duas estruturas funcionem em Python, elas não são boas maneiras de se nomear 
variáveis em Python. Esta maneira de nomear variáveis é chamada de “snake case”, porque conectamos as 
palavras com sublinhados.
'''

#==================================================================#
''''
Bitwise operators
Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.
For example, 2 is 10 in binary and 7 is 111.
In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
'''        
        #Bitwise operators in Python
#Operator   Meaning	                Example
'''
&	        Bitwise AND	            x& y = 0 (0000 0000)
|	        Bitwise OR  	        x | y = 14 (0000 1110)
~	        Bitwise NOT 	        ~x = -11 (1111 0101)
^	        Bitwise XOR 	        x ^ y = 14 (0000 1110)
>>	        Bitwise right shift	    x>> 2 = 2 (0000 0010)
<<	        Bitwise left shift	    x<< 2 = 40 (0010 1000)
'''

    #Assignment operators in Python
#Operator	Example	    Equivatent to
'''
=	        x = 5	    x = 5
+=	        x += 5	    x = x + 5
-=	        x -= 5	    x = x - 5
*=	        x *= 5	    x = x * 5
/=	        x /= 5	    x = x / 5
%=	        x %= 5	    x = x % 5
//=	        x //= 5	    x = x // 5
**=	        x **= 5	    x = x ** 5
&=	        x &= 5	    x = x & 5
|=	        x |= 5	    x = x | 5
^=	        x ^= 5	    x = x ^ 5
>>=	        x >>= 5	    x = x >> 5
<<=	        x <<= 5	    x = x << 5
'''

                                #Identity operators in Python
#Operator	                        Meaning	                                            Example
'''
is	        True if the operands are identical (refer to the same object)	            x is True
is not	    True if the operands are not identical (do not refer to the same object)	x is not True
'''

#PORCENTAGEM
salário = 1500
aumento = 10
print (salário + (salário * aumento / 100))