# src/priority_queue.py

class PriorityQueue:
    def __init__(self):
        # Cada índice representa una cola de prioridad:
        # 0 = prioridad 1 (alta), 1 = prioridad 2 (media), 2 = prioridad 3 (baja)
        self.queues = [[] for _ in range(3)]

    def encolar(self, alerta):
        prioridad = alerta.priority
        if prioridad not in [1, 2, 3]:
            raise ValueError("Prioridad inválida. Debe ser 1, 2 o 3.")
        self.queues[prioridad - 1].append(alerta)

    def desencolar(self):
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        return None  # Todas las colas están vacías

    def esta_vacia(self):
        return all(len(q) == 0 for q in self.queues)

    def obtener_todas(self):
        # Retorna todas las alertas en orden de prioridad
        resultado = []
        for queue in self.queues:
            resultado.extend(queue)
        return resultado

    def __len__(self):
        return sum(len(q) for q in self.queues)


# Implementar una cola de prioridad personalizada para almacenar y organizar alertas según su nivel de prioridad:

#    Prioridad 1 = alta (va primero)
#    Prioridad 2 = media
#    Prioridad 3 = baja (va al final)