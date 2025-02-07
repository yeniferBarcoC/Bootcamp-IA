"""Importar libreria panda, fundamental para el analisis de datos"""
import Panda as pd

"""Ruta del archivo csv que contiene los datos
Si el archivo essta en el mismo directorio del Script, bata con poner el nombre del archivo
"""
path = "Online_Retail.csv"

"""Lee el archivo csv usando la funcion  'read_csv' de pandas
Se especifica la codificacion'latin1' (Tambien conocida como ISO-8859-1)
para manejar caracteres especiales
"""
retail_data = pd.read_csv(path, encoding="latin1")

"""Muestra el tipo de la variable 'retail_data' para confirmar que es un DataFrame.
Un DataFrame es una estructura de datos bidimensional (filas y columnas) similar a una tabla
"""
print(type(retail_data))


"""Imprime todo el conenido del DataFrame 'retail_data' para visualizar los datos que 
fueron leidos del archivo csv
"""
print(retail_data)
