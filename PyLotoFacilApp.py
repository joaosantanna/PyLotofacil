"""
Projeto: PyLogoFacil App
Descrição : O aplicativo  gerencia jogos da lotofacil - loteria da caixa economica federal

Modulo: Principal - tem a interface principal do programa

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1
Data : Outubro de 2019
"""
import PySimpleGUI as sg
from dialogos_suporte import dialogo_nova_aposta
from dados import Apostas

ap = Apostas()

# sg.ChangeLookAndFeel('BlueMono')
janela = sg.Window('PyLotoFacil App', size=(700, 400), font=('Helvetica', 11))

# ------ Menu Definition ------ #

menu_def = [
    ['Arquivo', ['Novo', 'Salvar', 'Sair']],
    ['Sobre'],
]

# definicao das colunas

col1 = [
    [sg.T('Menu de apostas')],
    [sg.B('Nova', size=(10, 1))],
    [sg.B('Editar', size=(10, 1))],
    [sg.B('Apagar', size=(10, 1))],
    [sg.B('Conferir', size=(10, 1))],
    [sg.B('Estatisticas', size=(10, 1))]
]
col2 = [
    [sg.T('Lista de apostas', font=('Helvetica', 12))],
    [sg.Listbox(values=[], size=(100, 15), auto_size_text=True, key='lista_de_apostas')]
]

# layout do aplicativo

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('PyLotoFacil', size=(30, 1), justification='center', font=("Helvetica", 25))],
    [sg.Column(col1, size=(200, 300)), sg.Column(col2, size=(500, 300))],
    [sg.Exit(size=(10, 1))]
]

janela.Layout(layout)

while True:
    evento, valores = janela.Read()

    if evento == 'Sair' or evento == 'Exit':
        break

    if evento == 'Nova':
        '''
        realiza nova aposta
        '''
        aposta = dialogo_nova_aposta()
        if aposta == 0:
            pass
        else:
            ap.nova_aposta(aposta)
            valores = ap.get_lista_apostas()
            janela.FindElement('lista_de_apostas').Update(valores)

janela.close()
