'''Código ASCII
O ASCII é um código que foi proposto por Robert W. Bemer como uma solução para unificar a representação de caracteres
alfanuméricos em computadores. Antes de 1960 cada computador utilizava uma regra diferente para representar estes
caracteres e o código ASCII nasceu para se tornar comum entre todas as máquinas.

O nome ASCII vem do inglês American Standard Code for Information Interchange ou ”Código Padrão Americano para o
Intercâmbio de Informação”. Ele é baseado no alfabeto romano e sua função é padronizar a forma como os computadores
representam letras, números, acentos, sinais diversos e alguns códigos de controle. No ASCII existem apenas 95
caracteres que podem ser impressos, eles são numerados de 32 a 126 sendo os caracteres de 0 a 31 reservados para
funções de controle.

Elabore um programa que apresente o código ASCII de um caracter de entrada.


A Entrada consiste de:
Uma string que consiste em um único caracter.

A Saída deve apresentar:
O código ASCII desse caracter.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Existe uma função embutida no Python para resolver isso. Investigue!

Descrição dos Exemplos:
No primeiro exemplo, o código ASCII do caracter "g" é 103.
No segundo exemplo, o código ASCII do caracter "G" é 103.'''


letra = str(input())
print(ord(letra))