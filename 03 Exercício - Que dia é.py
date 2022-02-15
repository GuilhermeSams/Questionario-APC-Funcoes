'''Que dia é?
A biblioteca do Python oferece módulos embutidos que fornecem acesso à funcionalidades do sistema e também módulos que fornecem soluções padronizadas para muitos problemas que ocorrem em programação cotidiana.

Analise o código abaixo, estude as funções apresentadas e selecione a opção correta:

from datetime import date
from datetime import timedelta

data1 = date.today()
print(data1)

data2 = data1 - timedelta(days = 1)
print(data2)
Observações:
Para este tipo de questão você só tem uma chance!
Rode o programa para analisar como ele se comporta!'''


from datetime import date
from datetime import timedelta

data1 = date.today()
print(data1)

data2 = data1 - timedelta(days = 1)
print(data2)

#esse codigo apresenta a data de ontem!