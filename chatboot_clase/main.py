"""
------------------------------------------------------------------------------------------------------
Importamos las librerias que seran necesarias en el proyecto
------------------------------------------------------------------------------------------------------
"""
from fastapi import FastAPI, Body # Importa la clase FastAPI del Framework FastAPI e importamos la clase Body
from fastapi.responses import HTMLResponse #Importa la clase HTMLResponse de la libreria fastapi


"""
------------------------------------------------------------------------------------------------------
Importamos las librerias que seran necesarias en el proyecto
------------------------------------------------------------------------------------------------------
"""

app = FastAPI() # Crea una instancia de la clase FastAPI

app.title = "Aplicacion de Peliculas" #Asigna el valor de title a la instancia de la clase FastAPI
app.version = "0.0.1"

"""
------------------------------------------------------------------------------------------------------
crearemos una variable llamada movies_list que va a ser igual a una lista la cual contendrá varios 
diccionarios que contendrán la información de las películas
------------------------------------------------------------------------------------------------------
"""
movies_list = [
    {
        "id":1,
        "title":"Deadpool y Wolverine",
        "overview": "Deadpool se retira, pero regresa para salvar a sus seres queridos y al mundo, con la ayuda de wolverine",
        "year": "2024",
        "rating": 9.5
        "category": "Acción"
    },
    {
        "id":2,
        "title":"Intensamente 2",
        "overview": "Riley enfrenta la adolescencia con nuevas emociones que confunden a las viejas",
        "year": "2024",
        "rating": 9.8
        "category": "Animación"
    }
]
#---------------------------------------GET-----------------------------------------------------------    
""" 
------------------------------------------------------------------------------------------------------
    Definimos la ruta de la API:
    "/": define la ruta a la que se debe dirigir la solicitud GET. En este caso '/' se refiere a la 
         raiz del sitio y cualquier solicitud GET a esa URL sera manejada por la funcion message().
    tags="Home": Esto lo podemos utilizar para agrupar determinadas rutas en nuestra aplicación
------------------------------------------------------------------------------------------------------
"""
@app.get('/', tags=["Home"])
def message(): # Definimos una función de la ruta
    #devolvemos un string en la repuesta de la ruta. retorna un objeto de la clase HTMLResponse
    #return ("Bienvenido al chatbot de Peliculas del Bootcamp de IA 2025") 
    return HTMLResponse('<h1> Hello World </h1>')

"""
------------------------------------------------------------------------------------------------------
Utilizando el mismo método get crearemos la ruta que almacenará las películas. La ruta será movies y 
la etiqueta movies. Luego, agregaremos la función que nos va  a devolver ese listado movies
------------------------------------------------------------------------------------------------------
"""
@app.get('/movies', tags=["Movies"]) #Definimos una ruta de la clase FastAPI
def movies():
    return movies_list

"""
------------------------------------------------------------------------------------------------------
Crearemos una nueva ruta llamada app.get y le vamos a decir que accederemos a movies y entre llaves 
poner el parámetro id luego va la función get_movie para acceder al parámetro.
------------------------------------------------------------------------------------------------------
"""
@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id:int):
    for item in movies_list:
        if item["id"] == id:
            return item
        return []

"""
------------------------------------------------------------------------------------------------------
Crearemos una nueva ruta que se va a llamar app.get y que va a acceder a movies. Realizaremos un 
filtrado de películas por categorías
------------------------------------------------------------------------------------------------------
""" 
@app.get('/movies/', tags=["Movies"])
def get_movies_by_category(category:str, year:int):
    #return category
    return [item for item in movies_list if item['category'] == category]

#---------------------------------------POST----------------------------------------------------------
"""POST se emplea cuando se quiere crear o agregar nuevos recursos en el servidor, como añadir un nuevo 
registro a una base de datos"""
@app.post('/movies', tags=["Movies"])
def create_movie(id: int=Body(), title: str=Body(), overview: str=Body(), year: int=Body(), rating: float=Body(), category: str=Body()):
    movies_list.append({
        "id":id,
        "title":title,
        "overview": overview,
        "year": year,
        "rating": category
    })
    return movies_list

#---------------------------------------PUT----------------------------------------------------------
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int=Body(), title: str=Body(), overview: str=Body(), year: int=Body(), rating: float=Body(), category: str=Body()):
    for item in movies_list:
        if item["id"] == id:
            item["id"]==id,
            item["title"]==title,
            item["overview"]== overview,
            item["year"]== year,
            item["rating"]== category
            return movies_list
    
#---------------------------------------DELETE-------------------------------------------------------
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id:int):
    for item in movies_list:
        if item["id"] == id:
            movies_list.remove(item)
            return movies_list