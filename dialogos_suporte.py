"""
Projeto: PyLogoFacil App
Descrição : O aplicativo  gerencia jogos da lotofacil - loteria da caixa economica federal

Modulo: Dialogos de suporte da aplicacao , são chamados a partir da interface
principal do programa.

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1
Data : Outubro de 2019
"""

import PySimpleGUIQt as sg

Tbotao = size=(20, 1)
fonte = ('Courier', 20)
def dialogo_nova_aposta():
    janela2 = sg.Window('Nova Aposta', font=fonte)

    layout = criar_grid_aposta('Nova aposta')

    janela2 = janela2.Layout(layout)

    while True:
        evento, valores = janela2.Read()

        if evento == 'OK':
            aposta = []
            # vou transformar a resposta em uma lista de numeros
            for i, v in enumerate(valores.values()):
                if v:
                    aposta.append(i + 1)

            checagem = checar_aposta(aposta)  # retorna true se tiver problema ( aposta < 15 )

            if checagem == 'Yes':  # confirma que aposta é maior que de 15 numeros 16 por exemplo
                janela2.Close()
                return aposta
            elif checagem:
                pass  # nao faz nada e nem fecha a janela
            else:
                janela2.Close()
                return aposta
        if evento == 'Cancelar':
            janela2.Close()
            return 0


def criar_grid_aposta(texto):
    grid = [[sg.T(texto)]]
    contador = 1
    for l in range(5):
        tmp = []
        for c in range(5):
            tmp.append(sg.Checkbox(str(contador), size=(5, 2)))
            contador += 1
        grid.append(tmp)

    botoes = [sg.B('OK', size=Tbotao), sg.B('Cancelar', size=Tbotao)]
    grid.append(botoes)
    return grid



def checar_aposta(lista_de_numeros):
    if len(lista_de_numeros) < 15:
        sg.PopupError('Quantidade de numeros apostados menor que 15!',
                      title='Erro na quantidade de numeros',
                      font= fonte)
        return True
    elif len(lista_de_numeros) > 15:
        resposta = sg.PopupYesNo('Quantidade de numeros apostados maior que 15 você confirma a aposta?',
                                 title='Duvida ?',
                                 font=fonte)
        return resposta
