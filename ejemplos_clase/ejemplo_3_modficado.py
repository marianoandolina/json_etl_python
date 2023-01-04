#!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

import json
import requests

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data


def transform(data):
    # Transformar los datos en dos vectores
    # para graficar
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['time']
    55.01
    '''
    x = [d['time'] for d in data]  
    y = [d['signal'] for d in data]
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['signal']
    794
    '''
    return x, y


def load(x ,y):
    pass





if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #
    print('# ---- Ejemplos con JSON ETL ---- #')

    # Crear el gráfico
    data = []
    #!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

import json
import requests

import matplotlib.pyplot as plt

def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data


def transform(data):
    # Transformar los datos en dos vectores
    # para graficar
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['time']
    55.01
    '''
    x = [d['time'] for d in data]  
    y = [d['signal'] for d in data]
    '''
    data =[{"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100},....]
    d = {"time": 55.01,"signal": 794,"peak": 0,"hr": 70.03891050583658,"sample_rate": 100}
    d['signal']
    794
    '''
    return x, y


def load(x ,y):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y)
    plt.show()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print('# ---- Ejemplos con JSON ETL ---- #')
   
    # Leer la data del sensor en la nube
    url = 'http://inove.pythonanywhere.com/monitor/sensor'
    data = extract(url)

    # Transformar la información para graficar
    x, y = transform(data)

    # Graficar la anumación
    load(x, y)

    print("Terminamos")