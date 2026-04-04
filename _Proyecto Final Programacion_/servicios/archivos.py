import json
import csv
import os

def cargar_desde_json(ruta):
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos
    except Exception as e:
        print("Error al cargar JSON: " + str(e))
        return []

def cargar_desde_csv(ruta):
    datos = []
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertimos tipos de datos del CSV (que siempre son texto)
            fila["id"] = int(fila["id"])
            fila["precio"] = float(fila["precio"])
            fila["stock"] = int(fila["stock"])
            datos.append(fila)
        archivo.close()
        return datos
    except Exception as e:
        print("Error al cargar CSV: " + str(e))
        return []

def guardar_factura_generica(nombre, datos, formato):
    try:
        if formato == "json":
            archivo = open(nombre + ".json", "w", encoding="utf-8")
            json.dump(datos, archivo, indent=4)
            archivo.close()
        else:
            archivo = open(nombre + ".csv", "w", newline="", encoding="utf-8")
            escritor = csv.writer(archivo)
            escritor.writerow(["Cliente", datos["cliente"], "Fecha", datos["fecha"]])
            escritor.writerow(["Videojuego", "Precio"])
            for j in datos["videojuegos"]:
                escritor.writerow([j["nombre"], j["precio"]])
            escritor.writerow(["TOTAL", datos["total"]])
            archivo.close()
        print("Factura generada con éxito.")
    except Exception as e:
        print("Error al guardar: " + str(e))