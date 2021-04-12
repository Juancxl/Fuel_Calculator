# Fuel Calculator
# made in 2021
# Author: Juan Caires


import PySimpleGUI as sg
import math


#Layout
sg.theme("Dark Grey")

layout = [
    [sg.Text("Leader's race pace [min:sec.dec]: "), sg.Input(key='lapString')],
    [sg.Text('Race lenght [minutes]: '), sg.Input(key='raceTime')],
    [sg.Text('Fuel consumption [L/Lap]: '), sg.Input(key='fuelConsumption')],   
    [sg.Button('Calculate!')],
    [sg.Output(size = (50, 3), font = '\b',key= '-OUTPUT-')],
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

        minutes = values['lapString'].split(':', -1)[0]
        seconds = values['lapString'].split(':', -1)[1]

#        if type(minutes) != int and type(seconds) != int:
#            print(f'Error reading data. Please review your inputs.')

        averageLapInSeconds = (float(minutes) * 60) + float(seconds)

        raceTimeInSeconds = int(values['raceTime']) * 60

        lapsNumber = raceTimeInSeconds/averageLapInSeconds
        totalFuel = lapsNumber * float(values['fuelConsumption'])

        print(f'Estimated race laps: {math.ceil(lapsNumber)} laps')
        print(f'Total race fuel needed: {math.ceil(totalFuel)} Liters')
