"""
Projeto: PyLogoFacil App
Descrição : O aplicativo  gerencia jogos da lotofacil - loteria da caixa economica federal

Modulo: Dialogos de suporte da aplicacao , são chamados a partir da interface
principal do programa.

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1
Data : Outubro de 2019
"""

import PySimpleGUI as sg


def dialogo_nova_aposta():
    janela2 = sg.Window('Nova Aposta', font=('Helvetica', 11))
    r = criar_grid_aposta('Informe os numeros da nova aposta')
    # TODO: tentar ler toda vez que um checkbox for marcado e contar quantos ja foram marcados
    layout = r

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
            tmp.append(sg.Checkbox(contador, size=(3, 1)))
            contador += 1
        grid.append(tmp)

    botoes = [sg.B('OK'), sg.B('Cancelar')]
    grid.append(botoes)
    return grid


def checar_aposta(lista_de_numeros):
    if len(lista_de_numeros) < 15:
        sg.PopupError('Quantidade de numeros apostados menor que 15!', title='Erro na quantidade de numeros')
        return True
    elif len(lista_de_numeros) > 15:
        resposta = sg.PopupYesNo('Quantidade de numeros apostados maior que 15 você confirma a aposta?',
                                 title='Duvida ?')
        return resposta
