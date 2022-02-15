'''O prof. Fagundes comprou uma caixa com m pacotes de bolacha recheada para distribuí-los igualmente entre os n alunos da sua turma de Estruturas de Dados na Universidade de Brasília (UnB). Apesar dos alunos terem adorado essa surpresa, cada um consegue comer no máximo k pacotes de bolacha, portanto, alguns desses pacotes entregues por aluno podem sobrar. A generosa ideia do querido professor consiste em pegar esses pacotes restantes e entregá-los aos funcionários do Departamento de Ciência da Computação (CIC) da UnB.

Sabendo-se que cada aluno sempre recebe e come ao menos um pacote de bolacha, elabore uma função chamada pacotesDeBolacha que receba os três números inteiros m, n e k como parâmetros e imprime a quantidade mínima de pacotes de bolacha que serão entregues aos funcionários do CIC.


A Entrada consiste de:
A função pacotesDeBolacha deve ser chamada para valores arbitrários definidos nos casos de teste, que são três números inteiros m, n e k (1≤n≤104,n≤m≤104,;1≤k≤104 ) associados ao número total de pacotes de bolacha, a quantidade de alunos da turma e a quantos pacotes de bolacha cada aluno dessa turma consegue comer, respectivamente.

A Saída deve apresentar:
A função pacotesDeBolacha deve imprimir a quantidade mínima de pacotes de bolacha que serão entregues aos funcionários do CIC.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, existem 4 pacotes de bolacha, 4 alunos e cada aluno consegue comer um pacote de bolacha. Assim, não sobrarão pacotes de bolacha para serem distribuídos aos funcionários do CIC.
No segundo exemplo, existem 13 pacotes de bolacha e 5 alunos, sendo que cada aluno consegue comer k=2 pacotes de bolacha. Assim, tentando dividir igualmente os 13 pacotes para os 5 alunos, temos que cada aluno poderia comer 2 pacotes, o que é possível de acordo com k. Assim, a turma toda comerá 10 pacotes e restarão 3 pacotes para os funcionários do CIC.
No terceiro exemplo, existem 10 pacotes de bolacha e 9 alunos, sendo que cada aluno consegue comer k=2 pacotes de bolacha. A divisão igualitária dos pacotes entre os alunos diz que cada aluno come 1 pacote de bolacha, resultando em 9 pacotes para toda a turma. O pacote de bolacha restante é destinado aos funcionários do CIC.'''