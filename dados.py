class Apostas:

    def __init__(self):
        self.__apostas = []

    def nova_aposta(self, numeros):
        """
        metodo para criar aposta nova
        :param numeros: uma lista com os numeros da aposta
        :return: o numero de apostas cadastradas
        """
        self.__apostas.append(numeros)
        return len(self.__apostas)

    def update_aposta(self, posicao, numeros):
        """
        metodo para fazer atualizacoes nas apostas
        :param posicao: posicao na lista de apostas que vc quer modificar
        :param numeros: novos numeros de aposta para substituir os antigos
        :return: numero de apostas cadastradas
        """
        self.__apostas.pop(posicao)
        self.__apostas.insert(posicao, numeros)
        return len(self.__apostas)

    def apagar_aposta(self, posicao):
        """
        metodo para apagar apostas cadastradas
        :param posicao: posicao da aposta que deve ser apagada da lista de apostas
        :return: numero de apostas cadastradas
        """
        aposta_apagada = self.__apostas.pop(posicao)
        return aposta_apagada

    def numero_de_apostas(self):
        """
        metodo que retorna o numero de apostas cadastradas
        :return: numero de apostas cadastradas na lista
        """
        return len(self.__apostas)

    def get_aposta(self, posicao):
        """
        metodo para retornar uma aposta qualquer
        :param posicao: posicao da aposta que vc quer retornar
        :return: um conjunto de numeros apostados
        """
        return self.__apostas[posicao]

    def get_lista_apostas(self):
        """
        Metodo para passar uma lista com as apostas
        :return: Uma lista de tuplas , com o indentificador da aposta e os numeros apostados
        """
        resposta = []
        for i, v in enumerate(self.__apostas):
            texto = 'Aposta ' + str(i + 1) + ':' + str(v)
            resposta.append(texto)

        return resposta


    def confere_apostas(self, numeros_sorteados):
        """
        Metodo para conferir quantos acertos em cada aposta , baseando-se nos numeros sorteados
        :return: retorna uma lista de tuplas , em cada tupla contém o numero de acertos , e a lista
        dos numeros que sorteados na aposta
        """
        resposta = []
        numeros_sorteados = set(numeros_sorteados)

        for aposta in self.__apostas:
            acertos = numeros_sorteados.intersection(aposta)
            acertos = list(acertos)
            acertos.sort() # trabalhar com set nao garante a ordem dos numeros preciso ordenar antes de retornar
            quantidade_acertos = len(acertos)
            resposta.append((quantidade_acertos, acertos))

        return resposta
