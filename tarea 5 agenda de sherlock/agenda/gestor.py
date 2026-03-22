import os 
from .contacto import Contacto
from .persistencia import ManejadorArchivo

class GestorAgenda:
    def __init__(self):
        self.contactos = []
        self.archivo_actual = None
        self.tipo_archivo = None

    def cargar_datos(self, ruta, tipo):
        self.archivo_actual = ruta
        self.tipo_archivo = tipo
        
        if tipo == 'json':
            datos = ManejadorArchivo.cargar_json(ruta)
        else:
            datos = ManejadorArchivo.cargar_csv(ruta)
        
        self.contactos = [Contacto(**d) for d in datos]
        return len(self.contactos)

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        self._actualizar_archivo()

    def _actualizar_archivo(self):
        if not self.archivo_actual: return
        datos_para_guardar = [c.to_dict() for c in self.contactos]
        
        if self.tipo_archivo == 'json':
            ManejadorArchivo.guardar_json(self.archivo_actual, datos_para_guardar)
        else:
            ManejadorArchivo.guardar_csv(self.archivo_actual, datos_para_guardar)

    def buscar_por_nombre(self, texto):
        return [c for c in self.contactos if texto.lower() in c.nombre.lower()]

    def buscar_por_telefono(self, texto):
        return [c for c in self.contactos if texto in c.telefono]

    def calcular_promedio_edad(self):
        if not self.contactos: return 0
        return sum(c.edad for c in self.contactos) / len(self.contactos)

#----------------------------------------------------------------------
#Se usa os.path para evitar errores de "Archivo no encontrado" si la terminal 
#se abre desde una carpeta raíz distinta a la del proyecto (ej. desde GitHub).

    def cargar_datos(self, nombre_archivo, tipo):
    
        directorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.archivo_actual = os.path.join(directorio_base, nombre_archivo)
        self.tipo_archivo = tipo
        
        if tipo == 'json':
            datos = ManejadorArchivo.cargar_json(self.archivo_actual)
        else:
            datos = ManejadorArchivo.cargar_csv(self.archivo_actual)
        
        self.contactos = [Contacto(**d) for d in datos]
        return len(self.contactos)

    def _actualizar_archivo(self):
        if not self.archivo_actual: return
        datos_para_guardar = [c.to_dict() for c in self.contactos]
        
        if self.tipo_archivo == 'json':
            ManejadorArchivo.guardar_json(self.archivo_actual, datos_para_guardar)
        else:
            ManejadorArchivo.guardar_csv(self.archivo_actual, datos_para_guardar)