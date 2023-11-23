import PySimpleGUI as sg 

layout =  [  
    [
        sg.Input(key = "INPUT"),
        sg.Spin(["km/miles", "kg/livres", "sec/min"], key="UNITE"),
        sg.Button("Conversion", key= "CONVERSION")
    ],
    [sg.text("Output", key= "OUTPUT")]
]
window = sg.Window("Convertisseur", layout).read()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break 

    if event == "CONVERSION":
        input_value = values["INPUT"]
        if input_value.isnumeric():
            match values["UNITE"]:
                case "km/miles":
                    output = round(float(input_value)) * 0.6214,2
                    output_string = f"{input_value} km font {output} miles"

                case "kg/livres":
                    output = round(float(input_value)) * 2.20462,2
                    output_string = f"{input_value} kg font {output} livres"

                case "sec/min":
                    output = round(float(input_value)) / 60,2
                    output_string = f"{input_value} secondes font {output} minutes"

            window["OUTPUT"].update(output_string)
        else:   
            window["OUTPUT"].update("Veuillez entrer un nombre")

window.close()
