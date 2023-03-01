
def origem_destino_iguais(origem, destino, lista_de_erros):
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino nao podem ser iguais'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Nao inclua numeros nesse campo'


def validacao_datas(data_ida, data_volta, lista_de_erros):
    if data_ida > data_volta:
        lista_de_erros['data ida'] = 'Data invalida'


def validacao_data_pesquisa(data_ida, data_pesquisa, lista_de_erros):
    if data_ida < data_pesquisa:
        lista_de_erros['data ida'] = ' Data invalida '
