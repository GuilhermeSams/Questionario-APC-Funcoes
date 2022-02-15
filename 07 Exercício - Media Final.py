'''O programa abaixo apresenta o cálculo da nota final a partir de 3 notas de uma aluno de uma disciplina, onde a função calcular_media recebe as três notas e calcula a média ponderada levando em consideração os respectivos pesos de cada nota: A nota nota1 tem peso1, nota nota2 tem peso2 e nota nota3 tem peso3. Ao executar esse programa, é possível perceber que ele apresenta alguns erros. Analise o código e faça os ajustes necessários para que ele funcione corretamente. É necessário realizar mais de uma alteração para que ele funcione de acordo com os exemplos disponibilizados.

def calcular_media(nota1, nota2, nota3):
    nota_final = nota1*peso1 + nota2*peso2 + nota3*peso3/peso1+peso2+peso3
    print(f'Sua nota final é {nota_final}')

peso1 = 1
peso2 = 2
peso3 = 3

n1, n2, n3 = map(float, input().split())
calcular_media(n1, n2, n3, peso1, peso2, peso3)

A Entrada consiste de:
Três números reais positivos representando as notas de um aluno.

A Saída deve apresentar:
A média final do aluno.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.

Descrição dos Exemplos:
No primeiro exemplo, a média ponderada entre as notas 5, 6 e 7 é 6.333333333333333
'''

def calcular_media(nota1, nota2, nota3):
    nota_final = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
    print(f'Sua nota final é {nota_final:.2f}')


peso1 = 1
peso2 = 2
peso3 = 3

n1, n2, n3 = map(float, input().split())
calcular_media(n1, n2, n3)