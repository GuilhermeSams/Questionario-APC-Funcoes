'''Crie duas funções fala e repete que tem uma string nome como argumento.

A função fala imprime a mensagem "Oi," e a string nome.

Já a função repete chama a função fala, passando nome como argumento, imprime a mensagem "Repete, por favor! Não consigo
 te ouvir!" e chama a função fala, passando nome como argumento novamente.


A Entrada consiste de:
Não se aplica.

A Saída deve apresentar:
As mensagens com as string especificadas no enunciado.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, é chama a execução da função repete passando como parâmetro "José". Então a função repete chama a
função fala que imprime "Oi, José". Na sequência a função repete imprime "Repete, por favor! Não consigo te ouvir!". E
por fim a função fala é novamente chamada e imprime "Oi, José".'''


def fala(nome):
    print(f'Oi, {nome}')


def repete(nome):
    fala(f'{nome}')
    print("Repete, por favor! Não consigo te ouvir!")
    fala(f'{nome}')