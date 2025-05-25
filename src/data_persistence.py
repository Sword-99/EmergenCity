# src/data_persistence.py

import json
import os

class DataPersistence:
    def __init__(self, carpeta='data'):
        self.carpeta = carpeta
        if not os.path.exists(self.carpeta):
            os.makedirs(self.carpeta)

    def guardar(self, nombre_archivo, datos):
        ruta = os.path.join(self.carpeta, nombre_archivo)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar(self, nombre_archivo):
        ruta = os.path.join(self.carpeta, nombre_archivo)
        if not os.path.exists(ruta):
            return None
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)

    def eliminar(self, nombre_archivo):
        ruta = os.path.join(self.carpeta, nombre_archivo)
        if os.path.exists(ruta):
            os.remove(ruta)
            return True
        return False
