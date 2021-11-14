from calculator import a
import PySimpleGUI as sg
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK"), [sg.Button("LOL")]]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        print("lol")
        print(a)
        break

window.close()