import PySimpleGUI as sg 
from time import time 

sg.theme("black")
layout=[
    [sg.Push(),sg.Image("cross.png", pad = 0, enable_events= True, key= "CLOSE")],
    [sg.VPush()],
    [sg.Text("time", font = "Young 50", key ="TIME")],
    [   
        sg.Button("Start", button_color= ("#FFFFFF","#FF0000"), border_width = 0, key = "STARTSTOP"),
        sg.Button("Lap", button_color=("#FFFFFF","#ff0000"), border_width = 0, key = "LAP")
    ],
    [sg.VPush()]
]

window = sg.Window(
    "Chrono", layout,
    size = (300,300),
    no_titlebar = True,
    element_justification = "center")

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "CLOSE"):
        break

window.close()