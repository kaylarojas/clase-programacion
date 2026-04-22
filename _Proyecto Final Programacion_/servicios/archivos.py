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

# ESTA ES LA FUNCIÓN QUE TE FALTA SEGÚN EL ERROR:
def guardar_catalogo_completo(ruta, lista_objetos, formato):
    """
    Sobreescribe el archivo original (JSON o CSV) 
    con el estado actual de los objetos en memoria.
    """
    try:
        datos_planos = []
        for j in lista_objetos:
            datos_planos.append({
                "id": j.identificador,
                "nombre": j.nombre,
                "categoria": j.categoria,
                "precio": j.precio,
                "esrb": j.esrb,
                "stock": j.stock,
                "consola": j.consola
            })

        if formato == "1": # JSON
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos_planos, f, indent=4)
        
        elif formato == "2": # CSV
            with open(ruta, "w", newline="", encoding="utf-8") as f:
                columnas = ["id", "nombre", "categoria", "precio", "esrb", "stock", "consola"]
                escritor = csv.DictWriter(f, fieldnames=columnas)
                escritor.writeheader()
                escritor.writerows(datos_planos)
            
        print("--> Sincronización con archivo exitosa.")
    except Exception as e:
        print("Error al sincronizar con el archivo: " + str(e))