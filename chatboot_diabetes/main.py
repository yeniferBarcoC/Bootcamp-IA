# Importa la clase FastAPI del Framework FastAPI
from fastapi import FastAPI

# Crea una instancia de la clase FastAPI
app = FastAPI()

#Asigna el valor de title a la instancia de la clase FastAPI
app.title = "Diagnostico de Diabetes"
app.version = "0.0.1"

""" Definimos la ruta de la API:
    "/": define la ruta a la que se debe dirigir la solicitud GET. En este caso '/' se refiere a la raiz del sitio y 
         cualquier solicitud GET a esa URL sera manejada por la funcion message().
    tags="Home": Esto lo podemos utilizar para agrupar determinadas rutas en nuestra aplicación
"""
@app.get('/', tags=["Home"])

# Definimos una función de la ruta
def message():
    return("Bienvenido al chatbot de Diagnostico Diabetes del Bootcamp de IA 2025") # devolvemos un string en la repuesta de la ruta