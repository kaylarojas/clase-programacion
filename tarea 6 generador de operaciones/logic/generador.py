import random

def crear_ejercicios(cant_sumas, cant_restas, cant_mult, cant_div):
    practica = []
    respuestas = []

    config = [("+", cant_sumas), ("-", cant_restas), ("*", cant_mult), ("/", cant_div)]

    for simbolo, cantidad in config:
        for i in range(cantidad):
            n1 = random.randint(10, 99)
            n2 = random.randint(10, 99)

            if simbolo == "+":
                res = n1 + n2
            elif simbolo == "-":
                res = n1 - n2
            elif simbolo == "*":
                res = n1 * n2
            else: # División exacta
                res = n1
                n1 = n1 * n2

            linea_p = str(n1) + " " + simbolo + " " + str(n2) + " ="
            linea_r = str(n1) + " " + simbolo + " " + str(n2) + " = " + str(res)

            practica.append(linea_p)
            respuestas.append(linea_r)

    # Guardar archivos
    escribir_archivo("practica.txt", practica)
    escribir_archivo("respuestas.txt", respuestas)

def escribir_archivo(nombre, contenido):
    archivo = open(nombre, "w")
    for linea in contenido:
        archivo.write(linea + "\n")
    archivo.close()