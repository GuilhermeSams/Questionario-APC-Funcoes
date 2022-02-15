simbolo = str(input())


def multiplica_por_5(f):
    f()
    f()
    f()
    f()
    f()


def imprime_parteLinha():
    print("+-", end="")


def imprime_parte_linha_fim():
    print("+")


def imprime_parte_coluna():
    print(f'|{simbolo}', end="")


def imprime_parte_coluna_fim():
    print(f'|')


def imprime_linha():
    multiplica_por_5(imprime_parteLinha)
    imprime_parte_linha_fim()


def imprime_coluna():
    multiplica_por_5(imprime_parte_coluna)
    imprime_parte_coluna_fim()


def imprime_parte_celula():
    imprime_linha()
    imprime_coluna()


def imprime_tabela():
    multiplica_por_5(imprime_parte_celula)
    imprime_linha()


imprime_tabela()