"""
------------------------------ACTIVIDAD 4. CONTENEDORES EN PYTHON------------------------------
--------------------------------Modulo1. Unidad 2. Lección 1.----------------------------------

Contiene: * Presentacion de estructuras de datos cmo listas, tuplas, conjuntos, diccionarios.
          * Operaciones y métodos básicos para manejar los contenedores.

Autor: Yenifer Barco C
"""
#-----------------------------------------------------------------------------------------------
#------------------------------------------Página 7---------------------------------------------
#-----------------------------------------------------------------------------------------------

"""--------------------------------------------------------------------------------------------|
|2. TUPLAS: es otro tipo de contenedor, similar a una lista, pero con la diferencia principal  | 
|de que es inmutable, lo que significa que no puedes modificar su contenido después de haber   |
|sido creada. Las tuplas van en parentesis'()'.                                                |
|Se puede crear una tupla vacia con la palabra reservada 'tuple()' o tupla().                  |
|Las tuplas son útiles cuando necesitan asegurarse de que los datos no cambien durante la      |
|ejecución de su programa, y se utilizan comúnmente en situaciones donde la inmutabilidad es   |
|esencial.                                                                                     |
|----------------------------------------------------------------------------------------------|
|NOTA IMPORTANTE: el numero de variables debe ser igual al numero de elementos de la tupla. si |
| la tupla tiene 4 elementos, debe haber 4 variables.                                          |
|----------------------------------------------------------------------------------------------|
"""
# 2.1. Declaración de una Tupla
herramientas_de_goku = ("Baculo sagrado", "Nube voladora","Semillas del Ermitaño")
tuples = tuple(("Baculo sagrado", "Nube voladora","Semillas del Ermitaño"))
print("\n--------------------------TUPLAS----------------------------------------- ")
print("\n---------------Declaración de una Tupla:------------------- \n",herramientas_de_goku)

# 2.2. Indice y Acceso a los elementos: los elementos de una tupla también se numeran desde 0 en adelante.
herramienta1_de_goku = herramientas_de_goku[0]
herramienta2_de_goku = herramientas_de_goku[1]
print("\n---------------Indice y acceso a los elementos de una Tupla:------------------- \n", herramienta1_de_goku, herramienta2_de_goku)

#-----------------------------------------------------------------------------------------------
#------------------------------------------Página 8---------------------------------------------
#-----------------------------------------------------------------------------------------------

# 2.3 Longitud de una Tupla: puedes obtener la longitud de una tupla utilizando la función 'len()'.
cantidad_herramientas = len(herramientas_de_goku)
print("\n---------------Longitud de una Tupla:------------------- \n Cantidad herramientas de Goku:",cantidad_herramientas)

# 2.4. Inmutabilidad de las tuplas:	la principal diferencia con las listas es
# que las tuplas son inmutables, lo que significa que no pueden agregar, 
# eliminar o modificar elementos una vez que la tupla ha sido creada.

try: #control de errores de inmutabilidad.
    herramientas_de_goku[0] = " "
except:
    print("\n---------------Inmutabilidad de las Tuplas:------------------- \n",herramientas_de_goku)
    print("El elemento de la tupla no se puede modificar")

# 2.5. Empaquetado y desempaquetado de tuplas: pueden "empaquetar" varios valores en una tupla
# y luego "desempaquetar" esos valores en variables individuales.
# El empaquetado de tuplas es la acción de convertir una secuencia de elementos en una tupla.
# El desempaquetado de tuplas es laacción de convertir una tupla en una secuencia de elementos.
coordenadas = (1, 2, 3)
x, y, z = coordenadas
print("\n---------------Empaquetado y desempaquetado de tuplas:------------------- \n","Coordenadas: ",coordenadas, "x= {x}, y= {y}, z= {z}".format(x=x, y=y, z=z))

herramienta1_de_goku, herramienta2_de_goku, herramienta3_de_goku = herramientas_de_goku
print("Herramienta 1: {herramienta1_de_goku}, Herramienta 2: {herramienta2_de_goku}, Herramienta 3: {herramienta3_de_goku}".format(herramienta1_de_goku=herramienta1_de_goku, herramienta2_de_goku=herramienta2_de_goku, herramienta3_de_goku=herramienta3_de_goku))

#solucion con '*': si no sabes cuantos elementos quieres desempaquetar, puedes usar el asterisco '*'
herramienta1_de_goku, *restodeHerramientas = herramientas_de_goku
print("Herramienta 1: {herramienta1_de_goku}, Resto de herramientas: {restodeHerramientas}".format(herramienta1_de_goku=herramienta1_de_goku, restodeHerramientas=restodeHerramientas))

#-----------------------------------------------------------------------------------------------
#------------------------------------------Página 9---------------------------------------------
#-----------------------------------------------------------------------------------------------

# 2.6. USO EN ITERACIONES: las tuplas se utilizan comúnmente en situaciones donde se necesita una
# estructura de datos inmutable, como claves en un diccionario o elementos en un conjunto.

# 2.6.1. Tuplas anidadas: se pueden crear tuplas anidadas, que son tuplas que contienen otras tuplas.
mi_tupla = ("a", "b", "c", ("d", "e", "f"))
print("\n---------------Tuplas anidadas:------------------- \n", mi_tupla)

compañeros_goku = ("Goku", "Vegeta", "Trunks")
dragon_ball = (compañeros_goku, mi_tupla, herramientas_de_goku)
print(dragon_ball)

