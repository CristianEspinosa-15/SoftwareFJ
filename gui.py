"""
Módulo de Interfaz Gráfica (GUI) usando Tkinter.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from excepciones import SoftwareFJError

class AppGUI:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Gestión Software FJ - Fase 4")
        self.root.geometry("700x550")
        self.root.configure(padx=20, pady=20)

        # Título
        lbl_titulo = tk.Label(root, text="Sistema Integral Software FJ", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=(0, 10))

        lbl_sub = tk.Label(root, text="Demostración de POO y Excepciones Avanzadas", font=("Helvetica", 10, "italic"), fg="gray")
        lbl_sub.pack(pady=(0, 20))

        # Marco de Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(fill=tk.X, pady=10)

        btn_simular = tk.Button(frame_botones, text="▶ Ejecutar Simulación (10 Operaciones)", 
                                bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
                                command=self.ejecutar_simulacion)
        btn_simular.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar Consola", 
                                bg="#f44336", fg="white", font=("Helvetica", 10, "bold"),
                                command=self.limpiar_texto)
        btn_limpiar.pack(side=tk.RIGHT, padx=5)

        # Consola Visual (Área de texto desplazable)
        self.txt_consola = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Consolas", 10))
        self.txt_consola.pack(pady=10, fill=tk.BOTH, expand=True)
        self.txt_consola.configure(state='disabled') # Solo lectura

    def ejecutar_simulacion(self):
        try:
            # Llama al controlador para ejecutar la lógica de negocio
            self.sistema.ejecutar_simulacion()
            resultado = self.sistema.obtener_historial_simulacion()
            self.mostrar_texto(resultado)
            messagebox.showinfo("Éxito", "Simulación completada. Revisa la consola visual y el archivo sistema_logs.log")
        except SoftwareFJError as e:
            # Captura visual de excepciones no controladas en el gestor
            messagebox.showerror("Error del Sistema", str(e))
        except Exception as e:
            messagebox.showerror("Error Catastrófico", f"Error fatal: {e}")

    def mostrar_texto(self, texto):
        self.txt_consola.configure(state='normal')
        self.txt_consola.delete(1.0, tk.END)
        self.txt_consola.insert(tk.END, texto)
        self.txt_consola.configure(state='disabled')

    def limpiar_texto(self):
        self.mostrar_texto("")
