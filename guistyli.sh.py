from os import system 
import PySimpleGUI as sg


#Window
def window():
    sg.theme('DarkBlue8')
    layout = [
            [sg.Text('Window Manager: '),sg.Combo(['KDE','GNOME', 'XFCE', 'Sway', 'feh', 'nitrogen'], key='wm') ],
            [sg.Text('Theme: '), sg.Input(key='theme')],
            [sg.Text('Change the wallpaper hourly?'), sg.Checkbox('', key='always_change')],
            [sg.Button('Go!')]
            ]
    
    #Create Window
    return sg.Window('GUIStyli.sh', layout, finalize=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    ev, val = window().read()
    if ev == 'Go!':
        #Handle the WM
        if val['wm'] == 'feh':
            wm = ''
        elif val['wm'] == 'nitrogen':
            wm = '-n'
        elif val['wm'] == 'XFCE':
            wm = '-x'
        elif val['wm'] == 'KDE':
            wm = '-k'
        elif val['wm'] == 'Sway':
            wm = '-y'
        elif val['wm'] == 'GNOME':
            wm = '-g'

        #Other Features
        theme = f"-s {val['theme']}"
        if val['theme'] == '':
            theme = ''
        final_string = f"./styli.sh {wm} {theme}" 
        
        if val['always_change'] == False:
            system(final_string)
        
        else:
            #Keep changing wallpaper hourly
            set_interval = f"while [ 1 > 0 ]; do {final_string} && sleep 5; done  " 
            system(set_interval)
        window().hide()
    if ev == sg.WIN_CLOSED: 
        break


