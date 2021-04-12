# howManyLaps
# made in May/2020

from PySimpleGUI import PySimpleGUI as sg
import math

#Layout
sg.theme("Reddit")
layout = [
    [sg.Text("Leader's race pace [min:seg.dec]: "), sg.Input(key='lapString')],
    [sg.Text('Race lenght [minutes]: '), sg.Input(key='raceTime')],
    [sg.Text('Type your fuel consuptiom [L/Lap]: '), sg.Input(key='fuelConsumption')],   
    [sg.Button('Calculate!')],
    [sg.Output(size = (40, 20))],
]


#App window
window = sg.Window('Fuel Calculator', layout)


#Event reading and loop
while True:
    events, values = window.read()
#    lapString = str(input("Type the leader's rsace pace [min:seg.dec]: "))
#    raceTime = float(input("Type the race lenght [minutes]: "))
#    fuelConsumption = float(input("Type your car's fuel comsuption [L/Lap]: "))

    if events == sg.WINDOW_CLOSED:
        break

    minutes = values['lapString'].split(':', -1)[0]
    seconds = values['lapString'].split(':', -1)[1]

    averageLapInSeconds = (float(minutes) * 60) + float(seconds)

    raceTimeInSeconds = int(values['raceTime']) * 60

    lapsNumber = raceTimeInSeconds/averageLapInSeconds
    totalFuel = lapsNumber * float(values['fuelConsumption'])

    print(f'Estimated race laps: {math.ceil(lapsNumber)} laps')
    print(f'Total race fuel needed: {math.ceil(totalFuel)} Liters')
