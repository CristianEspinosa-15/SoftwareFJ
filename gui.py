"""
Módulo de Interfaz Gráfica de Usuario (gui.py)
----------------------------------------------
Utiliza la biblioteca Tkinter para crear una ventana de escritorio.
Se encarga exclusivamente de la capa visual (Patrón Vista en MVC).
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from excepciones import SoftwareFJError

class AppGUI:
    """Clase constructora de la ventana de la aplicación."""
    
    def __init__(self, root, sistema):
        # 'root' es la ventana base proveída por Tkinter
        self.root = root
        # 'sistema' es la instancia del gestor (Controlador) que realiza la lógica
        self.sistema = sistema
        
        # Configuración básica de la ventana
        self.root.title("Gestión Software FJ - Fase 4")
        self.root.geometry("700x550")
        self.root.configure(padx=20, pady=20)

        # Creación de Etiquetas (Labels) para el encabezado
        lbl_titulo = tk.Label(root, text="Sistema Integral Software FJ", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=(0, 10)) # pack() ubica el elemento en la ventana

        lbl_sub = tk.Label(root, text="Demostración de POO y Excepciones Avanzadas", font=("Helvetica", 10, "italic"), fg="gray")
        lbl_sub.pack(pady=(0, 20))

        # Marco (Frame) para contener y organizar los botones en línea horizontal
        frame_botones = tk.Frame(root)
        frame_botones.pack(fill=tk.X, pady=10)

        # Botón para detonar la simulación de las 10 operaciones
        btn_simular = tk.Button(frame_botones, text="▶ Ejecutar Simulación (10 Operaciones)", 
                                bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
                                command=self.ejecutar_simulacion) # Vincula el botón al método ejecutar_simulacion
        btn_simular.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Botón para limpiar la pantalla
        btn_limpiar = tk.Button(frame_botones, text="Limpiar Consola", 
                                bg="#f44336", fg="white", font=("Helvetica", 10, "bold"),
                                command=self.limpiar_texto)
        btn_limpiar.pack(side=tk.RIGHT, padx=5)

        # Consola Visual: Un widget de texto con barra de desplazamiento (Scroll)
        self.txt_consola = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Consolas", 10))
        self.txt_consola.pack(pady=10, fill=tk.BOTH, expand=True)
        # Se establece en 'disabled' para que el usuario no pueda escribir en él (Solo lectura)
        self.txt_consola.configure(state='disabled') 

    def ejecutar_simulacion(self):
        """
        Método puente. Invoca la lógica en el backend y maneja visualmente 
        cualquier error no previsto que haya subido hasta esta capa.
        """
        try:
            # Llama al controlador para ejecutar la lógica de negocio profunda
            self.sistema.ejecutar_simulacion()
            
            # Recupera el registro de la simulación y lo muestra en pantalla
            resultado = self.sistema.obtener_historial_simulacion()
            self.mostrar_texto(resultado)
            
            # Muestra un pop-up informando éxito
            messagebox.showinfo("Éxito", "Simulación completada. Revisa la consola visual y el archivo sistema_logs.log")
            
        except SoftwareFJError as e:
            # Captura visual: Si un error de nuestra lógica saltó hasta acá, se muestra en un cuadro de diálogo.
            messagebox.showerror("Error de Negocio del Sistema", str(e))
        except Exception as e:
            # Captura de último recurso para errores genéricos o fatales (ej. falta de memoria).
            messagebox.showerror("Error Catastrófico", f"Ocurrió un error inesperado de Python: {e}")

    def mostrar_texto(self, texto):
        """Habilita temporalmente la consola, inserta el texto y la vuelve a bloquear."""
        self.txt_consola.configure(state='normal')
        self.txt_consola.delete(1.0, tk.END) # Borra lo anterior
        self.txt_consola.insert(tk.END, texto) # Escribe lo nuevo
        self.txt_consola.configure(state='disabled') # Vuelve a bloquear

    def limpiar_texto(self):
        """Borra la consola visual a través de mostrar_texto vacío."""
        self.mostrar_texto("")
