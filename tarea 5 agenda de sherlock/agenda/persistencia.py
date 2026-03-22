import json
import csv

class ManejadorArchivo:
    @staticmethod
    def cargar_json(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def guardar_json(ruta, lista_dicts):
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(lista_dicts, f, indent=4)

    @staticmethod
    def cargar_csv(ruta):
        contactos = []
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    contactos.append(fila)
        except FileNotFoundError:
            pass
        return contactos

    @staticmethod
    def guardar_csv(ruta, lista_dicts):
        if not lista_dicts: return
        campos = lista_dicts[0].keys()
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(lista_dicts)