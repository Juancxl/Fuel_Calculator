# Fuel Calculator
# made in 2021
# Author: Juan Caires


import PySimpleGUI as sg
import math


#Layout
sg.theme("Dark Grey")

layout = [
    [sg.Text("Leader's race pace [min:sec]: "), sg.Input(key='lapString')],
    [sg.Text('Race lenght [minutes]: '), sg.Input(key='raceTime')],
    [sg.Text('Fuel consumption [L/Lap]: '), sg.Input(key='fuelConsumption')],   
    [sg.Button('Calculate!')],
    [sg.Output(size = (40, 5), font = '\b',key= '-OUTPUT-')],
]


#App window
window = sg.Window('Fuel Calculator', layout, icon=r'.\img\racing.ico')


#Event reading and loop
while True:
    events, values = window.read()

    if events == sg.WINDOW_CLOSED:
        break

    if events == 'Calculate!':
        window['-OUTPUT-'].update(value='')             # Clearing the output window

        try:                                            # Reading the user inputs
            minutes = values['lapString'].split(':', -1)[0]
            seconds = values['lapString'].split(':', -1)[1]

            if len(minutes) == 1 and len(seconds) == 2 and minutes.isnumeric() and seconds.isnumeric():    # Checking if the input data format is correct
                averageLapInSeconds = (float(minutes) * 60) + float(seconds)            # If yes, then the app will do his thing
                raceTimeInSeconds = int(values['raceTime']) * 60
                lapsNumber = raceTimeInSeconds/averageLapInSeconds
                totalFuel = lapsNumber * float(values['fuelConsumption'])
                safetyFuel = totalFuel + float(values['fuelConsumption'])               # Plus one lap of fuel, for safety
                print(f'Estimated race laps: {math.ceil(lapsNumber)} laps')
                print(f'Total race fuel needed: {math.ceil(totalFuel)} Liters')
                print(f'Safety ammount of fuel: {math.ceil(safetyFuel)} Liters')

            else:
                print(f'Data formats are wrong. Please review your inputs.')            # If not, the user will need to check his inputs

        except IndexError:                              # Something went wrong with the user inputs
            print(f'Error reading data. Please review your inputs.')
        except ValueError:                              # Something went wrong with the user inputs (2)
            print(f'Error reading data. Please review your inputs 1.')
