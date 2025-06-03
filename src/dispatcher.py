# src/dispatcher.py

import uuid

class UnidadMovil:
    def __init__(self, nombre):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.estado = "disponible"
        self.alerta_asignada = None

    def asignar_alerta(self, alerta):
        if self.estado == "ocupada":
            raise Exception("Unidad ya está ocupada.")
        self.alerta_asignada = alerta
        self.estado = "ocupada"

    def liberar(self):
        self.alerta_asignada = None
        self.estado = "disponible"

    def __str__(self):
        estado_info = f"Estado: {self.estado}"
        if self.alerta_asignada:
            estado_info += f" | Atendiendo: {self.alerta_asignada.incident_type}"
        return f"{self.nombre} ({estado_info})"

class Dispatcher:
    def __init__(self):
        self.unidades = []

    def registrar_unidad(self, nombre):
        unidad = UnidadMovil(nombre)
        self.unidades.append(unidad)
        return unidad

    def asignar_alerta_a_unidad(self, alerta):
        for unidad in self.unidades:
            if unidad.estado == "disponible":
                unidad.asignar_alerta(alerta)
                return unidad
        return None  # No hay unidades disponibles

    def liberar_unidad(self, unidad_id):
        for unidad in self.unidades:
            if unidad.id == unidad_id:
                unidad.liberar()
                return True
        return False

    def obtener_unidades_disponibles(self):
        return [u for u in self.unidades if u.estado == "disponible"]

    def obtener_unidades_ocupadas(self):
        return [u for u in self.unidades if u.estado == "ocupada"]

    def listar_todas_las_unidades(self):
        return self.unidades

# Función del módulo:

# Este módulo gestiona la asignación de unidades móviles a alertas activas, 
# verificando su disponibilidad y evitando que una unidad atienda más de una alerta al mismo tiempo.


# Lógica clave:

    # Cada unidad tiene:
        # - ID único
        # - Estado (disponible o ocupada)
        # - Alerta asignada (si está ocupada)

    # Cuando se asigna una alerta:
        # - Se busca la primera unidad disponible
        # - Se marca como ocupada
        # - Se enlaza con la alerta

    # También permite:
        # - Liberar una unidad
        # - Ver unidades disponibles/ocupadas