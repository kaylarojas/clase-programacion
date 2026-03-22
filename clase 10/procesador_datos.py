import csv
import json
import os

def leer_csv(ruta):
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    datos = []
    if not os.path.exists(ruta):
        return None
    
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        # DictReader usa la primera fila como llaves (edad, salario, peso)
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def leer_json(ruta):
    """Lee un archivo JSON y devuelve una lista de diccionarios."""
    if not os.path.exists(ruta):
        return None
        
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        return json.load(archivo)

def calcular_estadisticas(lista_personas):
    """Calcula promedios de edad, salario y peso."""
    if not lista_personas:
        return None
    
    suma_edad = 0
    suma_salario = 0
    suma_peso = 0
    total = len(lista_personas)

    try:
        for p in lista_personas:
            # Convertimos a float para asegurar que el cálculo matemático funcione
            suma_edad += float(p['edad'])
            suma_salario += float(p['salario'])
            suma_peso += float(p['peso'])

        return {
            "edad": suma_edad / total,
            "salario": suma_salario / total,
            "peso": suma_peso / total
        }
    except KeyError as e:
        print(f"Error: No se encontró la columna {e} en el archivo.")
        return None
    except ValueError:
        print("Error: Uno de los datos no es un número válido.")
        return None