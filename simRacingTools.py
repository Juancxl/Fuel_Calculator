# Sim Racing Tools
# Author: Juan Caires (Valete)


import PySimpleGUI as sg
import math

#User interface layouts

sg.theme("Dark Grey")


#Layout for the Fuel Calculator
layoutFuelCalc = [
    [sg.Text("Leader's race pace [min:sec]: "), sg.Input(key='lapString')],
    [sg.Text('Race length [minutes]: '), sg.Input(key='raceTime')],
    [sg.Text('Fuel consumption [L/Lap]: '), sg.Input(key='fuelConsumption')],   
    [sg.Button('Calculate fuel!')],
    [sg.Text("Estimated laps:", size=(15, 1), font='\b'),              sg.Text(key='lapsNumber', size=(10, 1), font='\b')],
    [sg.Text("Fuel needed:", size=(15, 1), font='\b'),                 sg.Text(key='totalFuel', size=(10, 1), font='\b')],
    [sg.Text("Safety fuel:", size=(15, 1), font='\b'),      sg.Text(key='safetyFuel', size=(10, 1), font='\b')],
]

# Layout for the Tyre Pressures calculator
# Right column (left side tyres)
col_11 = [
    [sg.Text('LF [PSI]'), sg.Input(key='lfPress', size= (10, 10))],
    [sg.Text(key='newLFPress', size=(10, 1), background_color='white', text_color='black')],
    [sg.Sizer(0, 150)],
    [sg.Text('LR [PSI]'), sg.Input(key='lrPress', size= (10, 10))],
    [sg.Text(key='newLRPress', size=(10, 1), background_color='white', text_color='black')]
]

# Center column (car image)
col_12 = [
    [sg.Image(r'D:\Projects\Python\Sim Racing Tools\img\racing_car.png')]
]

# Left column (right side tyres)
col_13 = [
    [sg.Text('RF [PSI]'), sg.Input(key='rfPress', size= (10, 10))],
    [sg.Text(key='newRFPress', size=(10, 1), background_color='white', text_color='black')],
    [sg.Sizer(0, 150)],
    [sg.Text('RR [PSI]'), sg.Input(key='rrPress', size= (10, 10))],
    [sg.Text(key='newRRPress', size=(10, 1), background_color='white', text_color='black')]
]

# Tyre Pressures Layout
layoutTyrePress = [
    [sg.Text('Only working for DRY conditions!')],
    [sg.Text('Track temp. [ºC]: '), sg.Input(key='givenTrackTemp')],
    [sg.Text('New track temp. [ºC]: '), sg.Input(key='newTrackTemp')],
    [sg.Button('Calculate tyre pressures!')],

    [sg.Frame(layout=col_11, title='Left side COLD press.'), 
    sg.Column(col_12, vertical_alignment='center', justification='center'), 
    sg.Frame(layout=col_13, title='Right side COLD press.')],
]


#Main Window Layout

mainLayout = [
    [sg.TabGroup([[sg.Tab('Fuel', layoutFuelCalc), sg.Tab('Tyre Pressures', layoutTyrePress)]])],
    [sg.Output(size = (40, 1), font = '\b',key= '-OUTPUT-')]
]

#App window

window = sg.Window('Sim Racing Tools', mainLayout, icon=r'.\img\racing.ico')


#Event reading and loop

while True:
    events, values = window.read()

    if events == sg.WINDOW_CLOSED:
        break

    #******************************************************************    
    # Fuel Calculation
    #******************************************************************

    if events == 'Calculate fuel!':
        window['-OUTPUT-'].update(value='')             # Clearing the output windows
        window['lapsNumber'].update(value='')
        window['totalFuel'].update(value='')
        window['safetyFuel'].update(value='')

        try:                                            # Reading the user inputs
            minutes = values['lapString'].split(':', -1)[0]
            seconds = values['lapString'].split(':', -1)[1]

            if len(minutes) == 1 and len(seconds) == 2 and minutes.isnumeric() and seconds.isnumeric():    # Checking if the input data format is correct
                averageLapInSeconds = (float(minutes) * 60) + float(seconds)            # If yes, then the app will do his thing
                raceTimeInSeconds = int(values['raceTime']) * 60
                lapsNumber = raceTimeInSeconds/averageLapInSeconds
                totalFuel = lapsNumber * float(values['fuelConsumption'])
                safetyFuel = totalFuel + float(values['fuelConsumption'])               # Plus one lap of fuel, for safety
                window['lapsNumber'].update(str(math.ceil(lapsNumber)) + " laps")
                window['totalFuel'].update(str(math.ceil(totalFuel)) + " Liters")
                window['safetyFuel'].update(str(math.ceil(safetyFuel)) + " Liters")
            else:
                print(f'Data formats are wrong. Please review your inputs.')            # If not, the user will need to check his inputs

        except IndexError:                              # Something went wrong with the user inputs
            print(f'Error reading Fuel data. Please review your inputs.')
        except ValueError:                              # Something went wrong with the user inputs (2)
            print(f'Error reading Fuel data. Please review your inputs. ')

    #******************************************************************    
    # Tyre Pressures Calculation
    #******************************************************************

    if events == 'Calculate tyre pressures!':
        window['-OUTPUT-'].update(value='')

        try:
            tempDiff = abs(int(values['givenTrackTemp']) - int(values['newTrackTemp']))
            if values['newTrackTemp'] < values['givenTrackTemp']:           # If the current track temperature is lesser then the given one
                newLFPress = float(values['lfPress']) + (0.1 * tempDiff)                
                newLRPress = float(values['lrPress']) + (0.1 * tempDiff)                
                newRFPress = float(values['rfPress']) + (0.1 * tempDiff)                
                newRRPress = float(values['rrPress']) + (0.1 * tempDiff)               
            else:                                                           # If its higher
                newLFPress = float(values['lfPress']) - (0.1 * tempDiff)                
                newLRPress = float(values['lrPress']) - (0.1 * tempDiff)                
                newRFPress = float(values['rfPress']) - (0.1 * tempDiff)                
                newRRPress = float(values['rrPress']) - (0.1 * tempDiff)             
            window['newLFPress'].update(newLFPress)
            window['newLRPress'].update(newLRPress)
            window['newRFPress'].update(newRFPress)
            window['newRRPress'].update(newRRPress)
        except IndexError:                              # Something went wrong with the user inputs
            print(f'Error reading Tyre data. Please review your inputs.')
        except ValueError:                              # Something went wrong with the user inputs (2)
            print(f'Error reading Tyre data. Please review your inputs. ')