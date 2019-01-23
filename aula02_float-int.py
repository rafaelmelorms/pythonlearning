
#Números inteiros e floats
'''
Há dois tipos de dados em Python que podem ser utilizados para valores numéricos:

int - para valores inteiros
float - para valores decimais ou de ponto flutuante
Você pode criar um valor que segue um determinado tipo de dados usando a seguinte sintaxe:
'''
x = int(4.7)   # x é inteiro que vale 4
y = float(4)   # y é um float com valor 4.0
#Você pode verificar o tipo, usando a função type:

print(type(x))
#int
print(type(y))
#float

#Como flutuação, ou aproximação, para 0,1 é, na verdade, um pouco maior do que 0,1, quando somamos vários dele podemos ver a diferença 
#entre a resposta matematicamente correta e a que o Python cria.

print(.1 + .1 + .1 == .3)
#Falso

