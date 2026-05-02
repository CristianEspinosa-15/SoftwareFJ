"""
Punto de Entrada - Software FJ
Ejecutar este archivo desde la consola (CMD) usando: python main.py
"""

import tkinter as tk
import logging
from sistema import SistemaGestion
from gui import AppGUI

def iniciar_aplicacion():
    try:
        # 1. Instanciamos el controlador lógico (Backend)
        sistema = SistemaGestion()
        
        # 2. Configuramos la ventana principal de Tkinter (Frontend)
        root = tk.Tk()
        
        # 3. Unimos Backend y Frontend
        app = AppGUI(root, sistema)
        
        logging.info("Aplicación con interfaz gráfica iniciada correctamente.")
        
        # 4. Bucle de ejecución visual
        root.mainloop()
        
    except Exception as e:
        # Protección de nivel superior en caso de que Tkinter falle
        print(f"Error crítico al iniciar la interfaz: {e}")
        logging.critical(f"Fallo de arranque de UI: {e}")

if __name__ == "__main__":
    iniciar_aplicacion()
