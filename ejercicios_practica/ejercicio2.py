# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.


    response = requests.get('https://jsonplaceholder.typicode.com/todos') 
    data = response.json()
    

    userid_1 = 0
    userid_2 = 0
    userid_3 = 0
    userid_4 = 0
    userid_5 = 0
    userid_6 = 0
    userid_7 = 0
    userid_8 = 0
    userid_9 = 0
    userid_10 = 0

    # print(data)

    for user in data:
        if user["userId"] == 1 and user["completed"] == True:
            userid_1 += 1
        if user["userId"] == 2 and user["completed"] == True:
            userid_2 += 1
        if user["userId"] == 3 and user["completed"] == True:
            userid_3 += 1
        if user["userId"] == 4 and user["completed"] == True:
            userid_4 += 1
        if user["userId"] == 5 and user["completed"] == True:
            userid_5 += 1
        if user["userId"] == 6 and user["completed"] == True:
            userid_6 += 1
        if user["userId"] == 7 and user["completed"] == True:
            userid_7 += 1
        if user["userId"] == 8 and user["completed"] == True:
            userid_8 += 1
        if user["userId"] == 9 and user["completed"] == True:
            userid_9 += 1
        if user["userId"] == 10 and user["completed"] == True:
            userid_10 += 1

print(f'''El UserId_1 completo {userid_1} titulos.\n El UserId_2 completo {userid_2} titulos.\n El UserId_3 completo {userid_3} titulos.\n
El UserId_4 completo {userid_4} titulos.\n El UserId_5 completo {userid_5} titulos.\n El UserId_6 completo {userid_6} titulos.\n El UserId_7 completo {userid_7} titulos.\n
El UserId_8 completo {userid_8} titulos.\n El UserId_9 completo {userid_9} titulos.\n El UserId_10 completo {userid_10} titulos.''')
    
x = list(range(1, 11))
y = [userid_1, userid_2, userid_3, userid_4, userid_5, userid_6, userid_7, userid_8, userid_9, userid_10]
# print(x)
# print(y)

fig = plt.figure()
ax = fig.add_subplot()

ax.bar(x, y, color='c', label= 'Titulos completados')
ax.set_facecolor('whitesmoke')
ax.set_title('Users y titulos completados')
ax.set_ylabel('Titulos completados')
ax.set_xlabel('Users Ids')
ax.grid(ls= 'dashed')
ax.set_yticks(range(0, 14,1))
ax.legend()

plt.show()

print("terminamos")
    