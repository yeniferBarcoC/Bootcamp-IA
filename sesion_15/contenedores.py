"""
------------------------------ACTIVIDAD 4. CONTENEDORES EN PYTHON------------------------------
--------------------------------Modulo1. Unidad 2. Lección 1.----------------------------------

Contiene: * Presentacion de estructuras de datos cmo listas, tuplas, conjuntos, diccionarios.
          * Operaciones y métodos básicos para manejar los contenedores.

Autor: Yenifer Barco C"""
          
#------------------------------------------Página 3---------------------------------------------

"""--------------------------------------------------------------------------------------------|
|1. LISTAS: es un contenedor flexible y mutable que permite almacenar una colecció n           |
|ordenada de elementos. Las listas van en corchetes'[]'.                                       |
|Las listas son herramientas versatiles en python y se utilizan comunmente para almacenar y    |
|manipular colecciones de datos                                                                |                    
|----------------------------------------------------------------------------------------------|
"""
# 1.1. Declaración de una lista
pokemones_de_ash = ["Pikachu","Carterpie", "Pidgey", "Charmander", "Squirtle"]
print("\n--------------------------LISTA---------------------------- ")
print("\n---------------Declaracion de una lista:------------------- ")
print(pokemones_de_ash)
print(pokemones_de_ash[0])

# 1.2. Indice y Acceso a los elementos de la lista: los elementos de una lista se numeran 
# desde 0 en adelante. Se accede a un elemento mediante su índice.
print("\n---------------Indice y acceso a los elementos de una lista:------------------- ")
primer_pokemon = pokemones_de_ash[0]
print(primer_pokemon)
segundo_pokemon = pokemones_de_ash[1]
print("El segundo pokemon de ash es {segundo_pokemon}")

#------------------------------------------Página 4---------------------------------------------

# 1.3. Longitud de la lista: Se puede obtener la longitud de una lista con la funcion len().
# la longitud de una lista es la cantidad de elementos que contiene una lista
cantidad_pokemones = len(pokemones_de_ash)
print("\n--------------Longitud de la lista:------------------- \n Cantidad de pokemones de ash:",cantidad_pokemones)

# 1.4. Modificacion de un elemento de la lista: Se puede modificar un elemento de una 
# lista mediante su indice
pokemones_de_ash[3] = "Tauros"
print("\n---------------Modificacion de un elemento de la lista:------------------- \n",pokemones_de_ash)

#------------------------------------------Página 5---------------------------------------------
# 1.5 OPERACIONES COMUNES EN LISTAS

# 1.5.1 Agregar un elemento al final de la lista: Se puede agregar un elemento
# al final de una lista con la funcion append()
pokemones_de_ash.append("Pidgeotto")
print("\n---------------Agregar un elemento al final de la lista:------------------- \n",pokemones_de_ash)  

# 1.5.2 Eliminar un elemento de la lista: Se puede eliminar un elemento de una
# lista con la funcion remove()
pokemones_de_ash.remove("Pidgey")
print("\n---------------Eliminar un elemento de la lista:------------------- \n",pokemones_de_ash)

# 1.5.3 Extender una lista con otra: Se puede extender una lista con otra con la
# funcion extend()
pokemones_de_ash.extend(["Pidgeot","Rattata",17,40])
print("\n---------------Extender una lista con otra:------------------- \n",pokemones_de_ash)

#RETO: Agregar los pokemosnes de Brock a la lista de pokemones de Ash
pokemones_de_brock = ["Onix", "Subat", "Crobat"]
pokemones_de_ash.extend(pokemones_de_brock)
print("RETO: Pokemones de Brock en Ash: ", pokemones_de_ash)

#------------------------------------------Página 6---------------------------------------------
# 1.5.4 Slicing (Rebanado): Se puede ontener un pedazo de la lista mediante el uso de slicing
batalla = pokemones_de_ash[1:3]
print("\n---------------SLICING(Recortando ó Rebanado):------------------- \n",batalla)

# 1.5.5 Inclusión de elementos: se puede verificar si un elemento se encuentra en una lista con el
# operador in
existe = "Tauros" in pokemones_de_ash
print("\n---------------Inclusion de elementos:------------------- \n", "Tauros" in pokemones_de_ash)


#------------------------------------------Página 7---------------------------------------------

"""--------------------------------------------------------------------------------------------|
|2. TUPLAS: es otro tipo de contenedor, similar a una lista, pero con la diferencia principal  | 
|de que es inmutable, lo que significa que no puedes modificar su contenido después de haber   |
|sido creada. Las tuplas van en parentesis'()'.                                                |
|----------------------------------------------------------------------------------------------|
"""
# 2.1. Declaración de una Tupla
mi_tupla = (1,2,3,'a','b','c')
print("\n---------------DECLARACION DE UNA TUPLA:------------------- ")

# 2.2. Indice y Acceso a los elementos: los elementos de una tupla también se numeran desde 0 en adelante.
primer_elemento = mi_tupla[0]
segundo_pokemon = mi_tupla[1]
print("\n---------------INDICE Y ACCESO A LOS ELEMENTOS DE UNA TUPLA:------------------- ")

# 2.3 Longitud de una Tupla: 
longitud = len(mi_tupla)
print("\n---------------LONGITUD DE LA TUPLA:------------------- \n Cantidad de pokemones de ash:",longitud)
