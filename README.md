# 🏢 Sistema Integral de Gestión - Software FJ (Modular con GUI)

## 📄 Descripción del Proyecto
Este proyecto es un sistema de gestión orientado a objetos desarrollado en **Python** para la empresa **Software FJ**.  
Esta versión destaca por su **arquitectura modular** y su **Interfaz Gráfica de Usuario (GUI)**, permitiendo una interacción visual sin perder el rigor técnico de la lógica de negocio.

El sistema está diseñado estrictamente **sin el uso de bases de datos**.  
La persistencia se simula en memoria y los errores se gestionan de forma avanzada, registrándose en el archivo `sistema_logs.log`.

---

## 📂 Arquitectura Modular
El proyecto ha sido refactorizado aplicando principios de diseño de software (**Separación de Responsabilidades**), dividido en los siguientes módulos:

- **`main.py`** → Punto de entrada de la aplicación. Inicializa la interfaz.  
- **`gui.py`** → Contiene toda la lógica visual (ventanas, botones, cajas de texto) usando **tkinter**.  
- **`sistema.py`** → Actúa como el controlador principal. Maneja las listas de datos y la simulación.  
- **`modelos.py`** → Contiene las clases de negocio (**Cliente, Reserva, Servicios**) aplicando herencia y polimorfismo.  
- **`excepciones.py`** → Define la jerarquía de errores personalizados.  

---

## 🛡️ Manejo de Excepciones en la Interfaz
Las excepciones (`ClienteInvalidoError`, `ReservaError`, etc.) no solo se registran en el archivo de logs,  
sino que la **interfaz gráfica** las captura y las muestra al usuario mediante cuadros de diálogo (**MessageBox**),  
demostrando visualmente el uso de bloques `try/except`.

---

## 🚀 Cómo ejecutar el proyecto
Sigue estos pasos para probar la simulación en tu máquina local:

1. Clona este repositorio en tu computadora.  
2. Abre una consola (**CMD** o **Terminal**) en la carpeta del proyecto.  
3. Ejecuta el inicializador principal con el comando:

   ```bash
   python main.py

4. Se abrirá la ventana principal. Haz clic en "Ejecutar Simulación Requerida" para procesar las 10 operaciones exigidas en la guía y observa los resultados en el panel visual.

---

## 📌 Nota
***Proyecto desarrollado para la Fase 4 del programa de Programación.***

---

