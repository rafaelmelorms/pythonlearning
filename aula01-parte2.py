# -*- coding: utf-8 -*-
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
