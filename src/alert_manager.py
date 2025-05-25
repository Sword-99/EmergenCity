# src/alert_manager.py

import uuid
from datetime import datetime

class Alert:
    def __init__(self, location, incident_type, priority):
        self.id = str(uuid.uuid4())
        self.location = location
        self.incident_type = incident_type
        self.priority = priority  # 1 = alta, 2 = media, 3 = baja
        self.timestamp = datetime.now().isoformat()
        self.status = "pendiente"  # o "resuelta"

    def __str__(self):
        return (f"[{self.priority}] Alerta {self.id[:8]} - "
                f"{self.incident_type} en {self.location} ({self.status})")

class AlertManager:
    def __init__(self):
        self.alerts = []

    def registrar_alerta(self, location, incident_type, priority):
        nueva_alerta = Alert(location, incident_type, priority)
        self.alerts.append(nueva_alerta)
        print(f"Alerta registrada:\n{nueva_alerta}")
        return nueva_alerta

    def listar_alertas(self, estado=None):
        if estado:
            return [a for a in self.alerts if a.status == estado]
        return self.alerts

    def resolver_alerta(self, alerta_id):
        for alerta in self.alerts:
            if alerta.id == alerta_id:
                if alerta.status == "resuelta":
                    print(f"Alerta ya estaba resuelta: {alerta_id}")
                else:
                    alerta.status = "resuelta"
                    print(f"✔️ Alerta resuelta: {alerta_id}")
                return True
        print(f"Alerta no encontrada: {alerta_id}")
        return False

    def eliminar_alertas_resueltas(self):
        antes = len(self.alerts)
        self.alerts = [a for a in self.alerts if a.status != "resuelta"]
        despues = len(self.alerts)
        print(f"Se eliminaron {antes - despues} alertas resueltas.")


# Funcionalidades incluidas:
# - Registro de una nueva alerta
# - Visualización de todas las alertas
# - Borrado de alertas resueltas (no pendientes)
# - Gestión de alertas (resolución y eliminación, luego se conecta con json)