import PySimpleGUI as sg

layout = [
    [sg.Text('Ola mundo', key='text')],
    [sg.Input(key='letra'), sg.Button('Btn3')]
]

tela = sg.Window('Minha primeira tela', layout)

while True:
    evento, valor = tela.read()

    if evento == 'Btn3':
        tela['text'].update(valor['letra'])
    

    if evento == sg.WIN_CLOSED:
        break
