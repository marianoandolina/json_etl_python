import json

json_2 = {
        "nombre": "Mariano", 
        "apellido": "Andolina", 
        "hijos": [
            {
                "firstname": "Oriana", "age": 8
            },
            {
                "firstname": "Brian", "age": 21
            }
        ]
        
}

json_string = json.dumps(json_2, indent= 4)



print(json_string)

# print(json_string)



print("terminamos")