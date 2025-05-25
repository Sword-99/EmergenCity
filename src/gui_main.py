# src/gui_main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from alert_manager import AlertManager
from priority_queue import PriorityQueue

class EmergenCityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EmergenCity - Atención de Emergencias")

        # Módulos internos
        self.alert_manager = AlertManager()
        self.priority_queue = PriorityQueue()

        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame de formulario
        formulario = tk.Frame(self.root, padx=10, pady=10)
        formulario.pack()

        tk.Label(formulario, text="Ubicación:").grid(row=0, column=0, sticky="w")
        self.ubicacion_entry = tk.Entry(formulario)
        self.ubicacion_entry.grid(row=0, column=1)

        tk.Label(formulario, text="Tipo de incidente:").grid(row=1, column=0, sticky="w")
        self.tipo_entry = tk.Entry(formulario)
        self.tipo_entry.grid(row=1, column=1)

        tk.Label(formulario, text="Prioridad:").grid(row=2, column=0, sticky="w")
        self.prioridad_combobox = ttk.Combobox(formulario, values=["1", "2", "3"])
        self.prioridad_combobox.current(0)
        self.prioridad_combobox.grid(row=2, column=1)

        tk.Button(formulario, text="Registrar alerta", command=self.registrar_alerta).grid(row=3, columnspan=2, pady=10)

        # Frame para lista de alertas
        self.lista_alertas = tk.Listbox(self.root, width=60)
        self.lista_alertas.pack(padx=10, pady=10)

    def registrar_alerta(self):
        ubicacion = self.ubicacion_entry.get()
        tipo = self.tipo_entry.get()
        prioridad = int(self.prioridad_combobox.get())

        if not ubicacion or not tipo:
            messagebox.showwarning("Campos incompletos", "Debes completar todos los campos.")
            return

        alerta = self.alert_manager.registrar_alerta(ubicacion, tipo, prioridad)
        self.priority_queue.encolar(alerta)
        self.actualizar_lista()

        self.ubicacion_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)

    def actualizar_lista(self):
        self.lista_alertas.delete(0, tk.END)
        alertas = self.priority_queue.obtener_todas()
        for alerta in alertas:
            self.lista_alertas.insert(tk.END, f"[{alerta.priority}] {alerta.incident_type} en {alerta.location} ({alerta.status})")


# Funcionalidad:

    # - Crear una ventana principal con menú
    # - Permitir el registro de una alerta desde la GUI
    # - Mostrar alertas en una lista