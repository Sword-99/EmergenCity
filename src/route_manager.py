# src/route_manager.py

class NodoRuta:
    def _init_(self, ubicacion):
        self.ubicacion = ubicacion
        self.siguiente = None
        self.anterior = None

class Ruta:
    def _init_(self):
        self.inicio = None
        self.fin = None

    def agregar_punto(self, ubicacion):
        nuevo_nodo = NodoRuta(ubicacion)
        if not self.inicio:
            self.inicio = self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.fin
            self.fin = nuevo_nodo

    def recorrer_ida(self):
        actual = self.inicio
        recorrido = []
        while actual:
            recorrido.append(actual.ubicacion)
            actual = actual.siguiente
        return recorrido

    def recorrer_retorno(self):
        actual = self.fin
        recorrido = []
        while actual:
            recorrido.append(actual.ubicacion)
            actual = actual.anterior
        return recorrido


# Funcionalidad del módulo:

#Simula una ruta de atención que puede recorrerse de ida y vuelta, usando una lista doblemente enlazada.
# Casos de uso:

    # - Registrar los puntos de una ruta (calles, intersecciones, etc.)
    # - Recorrer la ruta en orden (ida)
    # - Recorrerla en reversa (retorno)

# Estructuras implementadas:

    # - Nodo: con punteros a siguiente y anterior
    # - Ruta: con métodos para agregar y recorrer puntos