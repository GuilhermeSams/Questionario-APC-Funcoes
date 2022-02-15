'''Gael, um garotinho muito a frente de seu tempo, está aprendendo a programar. Ele fez um programa que denominou
 "modificador de números". O programa de Gael recebe um número inteiro n sendo 0≤n≤100  e o modifica 8 vezes: Gael
utiliza cada dígito do número de seu celular (87291365) para alterar o número recebido e retorna todas essas
possibilidades, para que ao final ele escolha a que mais o agradou. Veja abaixo:

n = int(input())
novo_n = n + 8
print(novo_n)
novo_n = n - 7
print(novo_n)
novo_n = n + 2
print(novo_n)
novo_n = n - 9
print(novo_n)
novo_n = n + 1
print(novo_n)
novo_n = n - 3
print(novo_n)
novo_n = n + 6
print(novo_n)
novo_n = n - 5
print(novo_n)
Gael percebeu que repetiu demais os símbolos matemáticos em seu programa e ficou insatisfeito com isso. Ele está ciente
 que você sabe modularizar um programa e pediu para que reescrevesse o código adicionando as funções soma e subtracao,
onde ambas devem receber os dois números da operação e mostrar o resultado após a realização dessas operações.


A Entrada consiste de:
Um número inteiro, que é o número que deve ser alterado.

A Saída deve apresentar:
Oito números inteiros, um em cada linha, sendo as oito possibilidades de alteração para o número n. Estes podem ser
positivos ou negativos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

Descrição dos Exemplos:
No primeiro exemplo, o n vale 12 e como a primeira alteração que ele sofre é a adição por 8, a primeira possibilidade é
20, a segunda possibilidade é 5, pois n é subtraído por 7 , seguem as operações e a última possibilidade é 7, resultado
da operação 12−5.
No segundo exemplo, o n vale 5 e como a primeira alteração que ele sofre é a adição por 8, a primeira possibilidade é
-2, a segunda possibilidade é 5, pois n é subtraído por 7 , seguem as operações e a última possibilidade é 0, resultado
da operação 5−5'''

n = int(input())


def soma():
    print(n + 8)
    print(n - 7)
    print(n + 2)
    print(n - 9)


def subtracao():
    print(n + 1)
    print(n - 3)
    print(n + 6)
    print(n - 5)


soma()
subtracao()