'''Todo mês, Mariângela, que trabalha no RH de uma empresa alimentícia, precisa fazer o cálculo do valor do auxílio
transporte que cada funcionário da empresa precisa receber. O cálculo é realizado da seguinte maneira: para cada dia
trabalhado o funcionário recebe 11 reais, valor referente a duas passagens, a de ida e de volta. Apesar desse padrão,
como alguns funcionários precisam pegar dois ônibus para chegar ao trabalho e dois para voltar para casa, no caso onde
o funcionário informa a empresa que precisa pegar mais dois ônibus, este funcionário recebe um acréscimo de 6 reais a
cada dia, passando então a receber 17 reais por dia de trabalho.

Com o sistema híbrido de trabalho, alguns dias certos funcionários trabalham em casa. O cálculo do auxílio transporte
considera apenas os dias que o funcionário trabalhou presencialmente.

Ajude Mariângela e escreva a função calcula, que recebe os dias de serviço de um funcionário no mês, a quantidade de
dias que ele trabalhou remotamente e uma flag que indica se o funcionário precisa pagar quatro passagens em um dia
(0 - ele não precisa, 1 - ele precisa). A função deve informar valor do auxílio transporte que o funcionário receberá.

A Entrada consiste de:
Não se aplica.

A Saída deve apresentar:
Um número inteiro que representa o valor do auxílio transporte que o funcionário deve receber.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Descrição dos Exemplos:
No primeiro exemplo, o funcionário trabalhou 20 dias e 4 foram remotos. Esse funcionário não precisa pegar quatro ônibus
por dia, então ele receberá 176, equivalente a 11 reais por 16 dias.
No segundo exemplo, o funcionário trabalhou 27 dias e 3 foram remotos, além disso ele informou que precisa pegar quatro
ônibus em um dia de trabalho, então ele receberá 264 reais pelos dias de trabalho presencial, mais um acréscimo de 144
das duas passagens diárias adicionais, totalizando 408 reais.'''