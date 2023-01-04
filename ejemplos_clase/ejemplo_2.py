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
import requests  # El metodo request permite hacer una peticion de informacion a una url


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")    
    print('# ---- Ejemplos con JSON Request ---- #')

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1") # Solicitamos la info a la url
    
    # Se puede obtener el objeto JSON de dos formas distintas
    # Forma nro 1
    '''De esta manera tenemos que buscar en que parte de la url esta la info en json y pasarla como parametro (respnse.text), en este caso en text esta la info
     en json de la url'''

    data = json.loads(response.text) 
    
    # Forma nro2 
    ''' La siguiente forma es la correcta porque es mas simple, con el metodo response.json() se encarga de buscar donde esta la info en formato json y guardarla
    en la variable'''
    
    data = response.json()

    print('Imprimir los datos traídos de la nube')
    print(json.dumps(data, indent=4))

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()

    for user in data:
        if user['userId'] > 2:
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes
            break
        print('El usuario {} completó {}? {}'.format(user['userId'],
                                                      user['title'],
                                                      user['completed']
                                                      ))

    print("terminamos")
