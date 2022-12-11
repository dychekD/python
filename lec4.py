# # model.py
# x = 0
# y = 0

# def init (a, b):
#     global x
#     global y
#     x = a
#     y = b

# def summa ():
#     return x+y


# #--------------

# # view.py
# def view_data (data):
#     print (data)

# def get_value ():
#     return int(input('value ='))

# #------------
# # controller.py

# #import modul
# #import view

# def button_click():
#     value_a = view.get_value ()
#     value_b = view.get_value ()
#     model.init (value_a, value_b)
#     result = model.sum()
#     view.view_data (result)

# #------------------

# # main.py

# #import controller
#  controller.button_click()

#-------------
# data_provider.py
from random import randint
def get_temperature (sensor):
    return randint (-20, 0) if sensor else randint (0, 20)

def get_pressure (sensor):
    return randint (720, 750) if sensor else randint (750, 770)

def get_wind_speed (sensor):
    return randint (0, 20) if sensor else randint (20, 50)

#------------
# logger.py

from datetime import datetime as dt

def temperature_logger (data):
    time = dt.now().strftime ('%H:%M')
    with open ('log.csv', 'a') as file:
        file.write ('{};temperature;{}'
                .format(time, data))

def pressure_logger (data):
    time = dt.now().strftime ('%H:%M')
    with open ('log.csv', 'a') as file:
        file.write ('{};pressure;{}'
                .format(time, data))

def wind_speed_logger (data):
    time = dt.now().strftime ('%H:%M')
    with open ('log.csv', 'a') as file:
        file.write ('{};wind_speed;{}'
                .format(time, data))

#------------
# user_interface.py

import data_provider as prov
import logger as log

def temp_view (sensor):
    data = prov.get_temperature(sensor)
    log.temperature_logger (data)
    return data

def press_view (sensor):
    data = prov.get_pressure(sensor)
    log.pressure_logger (data)
    return data

def ws_view (sensor):
    data = prov.get_wind_speed(sensor)
    log.wind_speed_logger (data)
    return data

#-----------------
# html_creator.py

from user_interface import temp_view
from user_interface import ws_view
from user_interface import press_view

def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temp_view(device))
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, ws_view(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, press_view(device))
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html



def new_create(data ,device = 1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '  </body>\n</html>'
    
    with open('new_index.html', 'w') as page:
        page.write(html)

    return data

#-------------
#main.py

import html_creator as hc
print (hc.create ())
