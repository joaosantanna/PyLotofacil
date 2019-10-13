"""
Projeto: PyLogoFacil App
Descrição : Aplicativo  gerencia jogos da lotofacil - loteria da caixa economica federal, atualizado para usar o PySimpleGUIQt para ter compatibilidade com o macosx ( a versao atual do PySimpleGUI 4.4.1 tem um bug no macOSX - reinicializa o sistema , memory falt)

Modulo: Principal - tem a interface principal do programa

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1
Data : Outubro de 2019
"""
import PySimpleGUIQt as sg
from dialogos_suporte import dialogo_nova_aposta
from dados import Apostas

ap = Apostas()

# sg.ChangeLookAndFeel('BlueMono')
janela = sg.Window('PyLotoFacil App', size=(700, 400), font=('Courier', 20))
sg.ChangeLookAndFeel('BlueMono')
# definicao das colunas

col1 = [
    [sg.T('Menu de apostas')],
    [sg.B('Nova', size=(20, 1))],
    [sg.B('Editar', size=(20, 1))],
    [sg.B('Apagar', size=(20, 1))],
    [sg.B('Conferir', size=(20, 1))],
    [sg.B('Estatisticas', size=(20, 1))]
]
col2 = [
    [sg.T('Lista de apostas', font=('Courier', 20))],
    [sg.Listbox(values=['Testando ', 'testando 2'], size=(400, 300), auto_size_text=True, key='lista_de_apostas')]
]

# layout do aplicativo

layout = [
    [sg.Column(col1), sg.Column(col2)],
    [sg.Exit(size=(10, 1))]
]

janela.layout(layout)

while True:
    evento, valores = janela.read()

    if evento == 'Exit':
        break
    elif evento == 'Nova':
        dialogo_nova_aposta()

janela.close()
