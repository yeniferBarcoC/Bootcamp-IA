"""Importaremos la libreria pandas que es fundamental
para el analisis de datos"""
import pandas as pd

"""Define la ruta del archivo donde se encuentran los datos"""
path = "Online_Retail.csv"

"""Leemos el archivo .csv con la libreria pandas"""
retail_data = pd.read_csv(path, encoding="latin-1", sep=",")

"""Imprimimos el dataframe"""
print(retail_data)