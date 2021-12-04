import PySimpleGUI as sg

sg.theme('dark Blue 3')

layout = [
    [sg.Text('Add URL'), sg.InputText(key='-Input-'), sg.Button('Insert')],
    [sg.Text('URL list')],
    [sg.Listbox(values=[], size=(40, 6), key='-Listbox-', enable_events=True), sg.Text('________'), sg.Button('Run'), sg.Text('________')],
    [sg.Button('Remove'), sg.Button('Exit')]
]

window = sg.Window('Dashboard', layout)

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    elif event == 'Insert':
        window['-Input-'].update('')
        window['-Listbox-'].update([])

    elif event == "Remove":
        selected_element = values['-Listbox-']
        if selected_element:
            window['-Listbox-'].update([])

window.close()
