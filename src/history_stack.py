# src/history_stack.py

from datetime import datetime

class HistorialAcciones:
    def __init__(self):
        self.stack = []

    def registrar_accion(self, accion):
        timestamp = datetime.now().isoformat()
        self.stack.append({"accion": accion, "fecha": timestamp})

    def obtener_ultima_accion(self):
        if self.stack:
            return self.stack[-1]
        return None

    def deshacer_ultima_accion(self):
        if self.stack:
            return self.stack.pop()
        return None

    def listar_historial(self):
        return list(reversed(self.stack))  # De más reciente a más antigua

    def esta_vacio(self):
        return len(self.stack) == 0


# Función del módulo:

# Registrar las acciones realizadas por una unidad móvil (como "despachada", "atendiendo", "retornando", etc.) 
# de manera que la última acción realizada esté siempre al tope de la pila.
# ¿Por qué una pila?

# Porque el historial debe poder:

    # - Agregar nuevas acciones fácilmente (push)
    # - Consultar la última acción realizada (peek)
    # - Deshacer o revisar la secuencia de acciones en orden inverso (pop)