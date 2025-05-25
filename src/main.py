# src/main.py

import tkinter as tk
from gui_main import EmergenCityGUI

def main():
    root = tk.Tk()
    app = EmergenCityGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# Primero, importamos la librería tkinter como tk.

# Luego, importamos la clase EmergenCityGUI desde el módulo gui_main.

# Definimos la función main()