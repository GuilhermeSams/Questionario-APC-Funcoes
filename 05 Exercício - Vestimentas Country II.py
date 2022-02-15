'''Vestimentas country II
Bonifácio é fã de moda country e isso fez com que ele adquirisse uma extensa coleção de botas e chapéus de diferentes
modelos. Em seu dia-a-dia, Bonifácio utiliza um jogo de vestimentas country, composto por duas peças: um chapéu e um par
 de botas. Agora Bonifácio precisa viajar para uma conferência no exterior e planeja incluir em sua bagagem o máximo de
  jogos de vestimentas country que puder.

Durante sua viagem, Bonifácio planeja utilizar todos os seus jogos de vestimenta country, mas com a restrição de que ele
veste um jogo apenas uma única vez e que não há distinção entre os chapéus e os pares de botas.

Sabe-se que Bonifácio possui em sua coleção de vestimentas x pares de botas e y chapéus, elabore uma função vestimentas
que receba os dois números inteiros x e y como parâmetros e calcule a quantidade máxima de peças nos jogos de
vestimentas country m que Bonifácio levará em sua bagagem.


A Entrada consiste de:
A entrada compreende os parâmetros da função vestimentas que são dois números inteiros x e y (1≤x≤102,1≤y≤102 )
 associados à quantidade x de pares de botas e y de chapéus, respectivamente.

A Saída deve apresentar:
A função vestimentas deve imprimir a quantidade máxima de peças nos jogos de vestimentas country que Bonifácio poderá
 levar na sua bagagem.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
 irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo teste, Bonifácio possui 2 chapéus e 2 pares de botas. Ele pode pegar um chapéu (qualquer um dos dois
 chapéus) e um par de botas (qualquer um dos pares de botas) e formar um jogo de vestimentas para ser utilizado em um
  dia. No dia seguinte, Bonifácio pega o chapéu e o par de botas restantes , formando um novo jogo. Ao final, ele conse
  gue formar dois jogos de vestimentas, resultando em 4 peças no total, conforme definição de que cada jogo possui 2 peças.
No segundo exemplo de teste, Bonifácio possui 4 chapéus e 1 par de botas. No primeiro dia, ele poderá pegar um chapéu
 (dentre os 4 disponíveis - pode ser qualquer chapéu) e formar um jogo de vestimenta com o único par de botas disponível
 . Não será possível formar outro jogo de vestimenta, pois não há outros pares de botas disponíveis. Veja que ele não
 repete peças já utilizadas em dias anteriores, resultando em 2 peças no total.
No exemplo de teste, Bonifácio possui 6 chapéus e 9 pares de botas. A partir desses 6 chapéus, ele consegue utilizá-lo
 com outros 6 pares de botas apenas, sem repetir as peças de vestimentas. Assim, o resultado é 12 peças no total.'''

def vestimentas(x, y):
    calculo = abs(x - y)
    m = ((x + y) - calculo)
    print(m)