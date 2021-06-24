from os import system 
#from time import sleep
import PySimpleGUI as sg
#import threading

        
#Window

sg.theme('DarkBlue8')
layout = [
        [sg.Text('Window Manager: '),sg.Combo(['KDE','GNOME', 'XFCE', 'Sway', 'feh', 'nitrogen'], key='wm') ],
        [sg.Text('Theme: '), sg.Input(key='theme')],
#        [sg.Text('Change the wallpaper hourly?'), sg.Checkbox('', key='always_change')], 
        [sg.Button('Change')]
        ]

#Create Window
window = sg.Window('GUIStyli.sh', layout, resizable=True, alpha_channel=0.87, icon="dog.png")

# Event Loop to process "events" and get the "values" of the inputs
while True:
    ev, val = window.read()
    if ev == sg.WIN_CLOSED: 
        break
    if ev == 'Change':
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
        system(final_string)
        
        #if val['always_change'] == False:
        #   system(final_string)
        
        #else:
        #    #Keep changing wallpaper hourly

        #    new_layout = [
        #            [sg.Text('Stop the change of wallpapers?')], 
        #            [sg.Button('Stop!')]
        #            ] 

        #    window.close()
        #    new_window = sg.Window('GUIStyli.sh', new_layout)
        #    ev2, val2 = new_window.read(timeout=1000)

        #    if ev2 == 'Stop!':
        #        break
          
         
