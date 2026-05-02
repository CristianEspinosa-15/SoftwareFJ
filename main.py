"""
Punto de Entrada Principal (main.py)
------------------------------------
Este archivo es el "Lanzador". Su única responsabilidad es arrancar la aplicación 
conectando las piezas (Backend con Frontend) e iniciando el bucle de eventos.
"""

import tkinter as tk
import logging
from sistema import SistemaGestion
from gui import AppGUI

def iniciar_aplicacion():
    """
    Función de arranque seguro. Organiza la inicialización de la arquitectura.
    """
    # Bloque TRY/EXCEPT maestro: El nivel más alto de la aplicación.
    # Evita que un error antes de abrir la ventana cierre la terminal de golpe.
    try:
        # 1. Instanciamos el controlador lógico (Backend/Gestor de datos)
        sistema = SistemaGestion()
        
        # 2. Instanciamos el motor visual base proveído por el sistema operativo vía Tkinter
        root = tk.Tk()
        
        # 3. Unimos Backend y Frontend inyectando el 'sistema' dentro de la GUI
        app = AppGUI(root, sistema)
        
        # Registro en Log de que el software inició con éxito
        logging.info("Aplicación con interfaz gráfica inicializada correctamente.")
        
        # 4. Inicia el 'Main Loop' (Bucle infinito de Tkinter que mantiene la ventana abierta y esperando clics)
        root.mainloop()
        
    except Exception as e:
        # Protección de nivel superior: Si Tkinter o el Gestor fallan catastróficamente al inicio.
        print(f"Error crítico durante el arranque de la aplicación: {e}")
        logging.critical(f"Fallo de arranque fatal: {e}")

if __name__ == "__main__":
    # Esta condición asegura que el código solo se ejecute si este archivo
    # se llama directamente (python main.py), y no si es importado por otro archivo.
    iniciar_aplicacion()
