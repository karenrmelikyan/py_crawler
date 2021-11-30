import PySimpleGUI as sg


def add_url(url):
    with open('gui/urls', 'a') as file:
        file.write(url + "\n")


def get_content():
    with open('gui/urls') as file:
        urls = file.read(9999).split("\n")
        urls.reverse()
        return urls


def remove_url(url):
    with open('gui/urls') as file:
        urls = file.read(9999).split("\n")
        urls.pop(len(urls) - 1)
        urls.remove(url)

    with open('gui/urls', 'w') as file:
        for url in urls:
            file.write(url + "\n")


sg.theme('dark Blue 3')

layout = [
    [sg.Text('Add URL'), sg.InputText(key='-Input-'), sg.Button('Insert')],
    [sg.Text('URL list')],
    [sg.Listbox(values=get_content(), size=(40, 6), key='-Listbox-', enable_events=True), sg.Text('________'), sg.Button('Run'), sg.Text('________')],
    [sg.Button('Remove'), sg.Button('Exit')]
]

window = sg.Window('Dashboard', layout)

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    elif event == 'Insert':
        add_url(values['-Input-'])
        window['-Input-'].update('')
        window['-Listbox-'].update(get_content())

    elif event == "Remove":
        selected_element = values['-Listbox-']
        if selected_element:
            remove_url(selected_element[0])
            window['-Listbox-'].update(get_content())

window.close()
