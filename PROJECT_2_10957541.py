import PySimpleGUI as sg
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Create the layout for the app interface
layout = [
    [sg.InputText(key="-INPUT-"),sg.Button("Speak", key="-SPEAK-")],
    [sg.Text("Enter text to speak:")],
    [sg.Text("Select a voice:"),sg.Radio("Male", "VOICE", default=True, key="-MALE-"),sg.Radio("Female", "VOICE", key="-FEMALE-")],
    [sg.Button("Exit", key="-EXIT-")]
    
]

# Create the PySimpleGUI window
window = sg.Window("Text-to-Speech App", layout)

# Create the event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-EXIT-":
        break
    if event == "-SPEAK-":
        text = values["-INPUT-"]
        voice_id = None
        if values["-MALE-"]:
            voice_id = 0 # Male voice index
        elif values["-FEMALE-"]:
            voice_id = 1 # Female voice index
        if voice_id is not None:
            engine.setProperty('voice', voices[voice_id].id)
        engine.say(text)
        engine.runAndWait()

# Close the PySimpleGUI window and the text-to-speech engine
window.close()
engine.stop()