"""Importar la libreria csv para trabajar con archivos csv"""
import csv

"""Leer los datos del archivo csv"""
with open('videos.csv', 'r') as file:  
    reader = csv.DictReader(file)   #Convertir cada registro en un diccionario
    videos = list(reader)           #Convertir el diccionario en una lista

"""Encontrar el video con la calificacion mas alta"""
mejor_video = max(videos, key=lambda x:float(x['Calificacion']))

"""Imprimir el video con la calificacion mas alta"""
print("🎥 Video Recomendado:")
print(f"Nombre: {mejor_video['Video']}")
print(f"Calificación: {mejor_video['Calificacion']}")
