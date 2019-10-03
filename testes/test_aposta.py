"""
arquivo de teste da classe aposta

"""
from dados import Apostas

ap = Apostas()


def test_nova_aposta():
    """
    Teste para criar uma nova aposta
    passa como argumento uma lista de numeros
    :return: 0 se não tiver nenhum erro
    """
    assert ap.nova_aposta([1, 2, 3, 4, 5]) == 1


def test_update_aposta():
    """
    Teste para atualizar uma aposta, chama o metodo de atualizacao
    depois verifica se a aposta foi atualizada para os novos numeros
    :return:
    """
    ap.update_aposta(0, [6, 7, 8, 9, 10])
    assert ap.get_aposta(0) == [6, 7, 8, 9, 10]


def test_remove_aposta():
    """
    teste para apagar apostas, primeiro cadastrei mais 2 apostas , verifiquei se agora eram 3 apostas
    e depois apaguei a aposta na posicao 1 e verifiquei se agora a lista de apostas tinha 2 entradas
    :return:
    """
    ap.nova_aposta([1, 2, 3, 4, 5, 6])
    ap.nova_aposta([10, 11, 12, 13, 14, 15])
    assert ap.numero_de_apostas() == 3
    assert ap.apagar_aposta(1) == [1, 2, 3, 4, 5, 6]

def test_get_aposta():
    """
    teste para pegar uma aposta
    :return:
    """
    assert ap.get_aposta(0) == [6, 7, 8, 9, 10]


def test_conferir_sorteio():
    """
    Teste para conferir se passando os numeros sorteados quanto cada aposta acertou e quais os numeros certos
    :return: uma lista de tuplas , na primeira posicao o numero de acertos e na segunda os numeros acertados
    """
    assert ap.numero_de_apostas() == 2
    assert ap.confere_apostas([6, 7, 10, 11]) == [(3, [6, 7, 10]), (2, [10, 11])]

