# src/gui_main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog  # <-- Agrega esta importación
from binary_tree import AlertBinaryTree  # <-- Agrega esta línea
import random  # <-- Agrega esta línea

from alert_manager import AlertManager
from priority_queue import PriorityQueue

class EmergenCityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EmergenCity - Atención de Emergencias")

        # Módulos internos
        self.alert_manager = AlertManager()
        self.priority_queue = PriorityQueue()
        self.alert_tree = AlertBinaryTree()  # <-- Agrega el árbol binario

        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear un Frame llamado formulario
        formulario = tk.Frame(self.root)
        formulario.pack(padx=10, pady=10)

        tk.Label(formulario, text="Ubicación:").grid(row=0, column=0, sticky="w")
        self.ubicacion_entry = tk.Entry(formulario)
        self.ubicacion_entry.grid(row=0, column=1)

        tk.Label(formulario, text="Tipo de incidente:").grid(row=1, column=0, sticky="w")
        self.tipo_combobox = ttk.Combobox(
            formulario,
            values=["Incendio", "Accidente de tráfico", "Emergencia médica", "Robo", "Otro"],
            state="readonly"
        )
        self.tipo_combobox.current(0)
        self.tipo_combobox.grid(row=1, column=1)

        tk.Label(formulario, text="Prioridad:").grid(row=2, column=0, sticky="w")
        self.prioridad_combobox = ttk.Combobox(formulario, values=["1", "2", "3"])
        self.prioridad_combobox.current(0)
        self.prioridad_combobox.grid(row=2, column=1)

        boton_registrar = tk.Button(formulario, text="Registrar alerta", command=self.registrar_alerta)
        boton_registrar.grid(row=3, columnspan=2, pady=10)

        # Botón "Enviar Emergencia"
        boton_enviar = tk.Button(formulario, text="Enviar Emergencia", command=self.enviar_emergencia, bg="#e74c3c", fg="white")
        boton_enviar.grid(row=4, columnspan=2, pady=5)

        # Frame para lista de alertas
        self.lista_alertas = tk.Listbox(self.root, width=60)
        self.lista_alertas.pack(padx=10, pady=10)

    def registrar_alerta(self):
        ubicacion = self.ubicacion_entry.get()
        tipo = self.tipo_combobox.get()
        prioridad = int(self.prioridad_combobox.get())

        if not ubicacion or not tipo:
            messagebox.showwarning("Campos incompletos", "Debes completar todos los campos.")
            return

        # Abrir ventana para descripción breve
        descripcion = simpledialog.askstring("Descripción", "Añade una descripción breve del accidente (opcional):", parent=self.root)
        if descripcion is None:
            # Si el usuario cancela, no registrar la alerta
            return

        alerta = self.alert_manager.registrar_alerta(ubicacion, tipo, prioridad, descripcion=descripcion)
        self.priority_queue.encolar(alerta)
        self.alert_tree.insert(alerta)  # <-- Inserta la alerta en el árbol
        self.actualizar_lista()

        self.ubicacion_entry.delete(0, tk.END)
        self.tipo_combobox.current(0)

    def actualizar_lista(self):
        self.lista_alertas.delete(0, tk.END)
        alertas = self.priority_queue.obtener_todas()
        for alerta in alertas:
            self.lista_alertas.insert(tk.END, f"[{alerta.priority}] {alerta.incident_type} en {alerta.location} ({alerta.status})")

    def enviar_emergencia(self):
        if self.alert_tree.is_empty():
            messagebox.showinfo("Sin alertas", "No hay alertas en el árbol para enviar.")
            return

        alerta = self.alert_tree.remove_root()
        prioridad = alerta.priority
        resultado = False

        if prioridad == 1:
            resultado = True
        elif prioridad == 2:
            resultado = random.random() < 0.6
        elif prioridad == 3:
            resultado = random.random() < 0.4

        msg = f"Alerta: {alerta.incident_type} en {alerta.location}\nPrioridad: {prioridad}\n"
        if resultado:
            msg += "✅ ¡Emergencia RESUELTA!"
            alerta.status = "resuelta"
        else:
            msg += "❌ No se pudo resolver la emergencia."

        messagebox.showinfo("Resultado de emergencia", msg)
        self.actualizar_lista()

    # - Mostrar alertas en una lista
# Funcionalidad:

    # - Crear una ventana principal con menú
    # - Permitir el registro de una alerta desde la GUI
    # - Mostrar alertas en una lista