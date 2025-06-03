# tests/test_priority_queue.py

import unittest
from src.priority_queue import PriorityQueue
from src.alert_manager import Alert

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue()

        # Crear alertas con distintas prioridades
        self.alerta1 = Alert("Zona A", "Incendio", 1)  # Alta prioridad
        self.alerta2 = Alert("Zona B", "Robo", 3)      # Baja prioridad
        self.alerta3 = Alert("Zona C", "Accidente", 2) # Media prioridad

    def test_encolar_y_orden(self):
        self.pq.encolar(self.alerta2)
        self.pq.encolar(self.alerta3)
        self.pq.encolar(self.alerta1)

        orden = [a.incident_type for a in self.pq.obtener_todas()]
        esperado = ["Incendio", "Accidente", "Robo"]
        self.assertEqual(orden, esperado)

    def test_desencolar(self):
        self.pq.encolar(self.alerta3)
        self.pq.encolar(self.alerta1)

        desencolada = self.pq.desencolar()
        self.assertEqual(desencolada.incident_type, "Incendio")

    def test_cola_vacia(self):
        self.assertTrue(self.pq.esta_vacia())
        self.pq.encolar(self.alerta1)
        self.assertFalse(self.pq.esta_vacia())
        self.pq.desencolar()
        self.assertTrue(self.pq.esta_vacia())

if __name__ == '__main__':
    unittest.main()
