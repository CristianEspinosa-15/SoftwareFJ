# 🏢 Sistema Integral de Gestión - Software FJ

## 📄 Descripción del Proyecto
Este proyecto es un sistema de gestión orientado a objetos desarrollado en **Python** para la empresa **Software FJ**.  
Permite la administración eficiente de **clientes**, **servicios** (salas, equipos y asesorías) y **reservas**.

El sistema está diseñado estrictamente **sin el uso de bases de datos**, almacenando la información en memoria mediante listas y objetos durante el tiempo de ejecución.  
Su principal fortaleza radica en el **manejo avanzado y robusto de excepciones**, garantizando que el programa nunca se detenga abruptamente y registrando cualquier anomalía de forma automática en un archivo de **logs**.

---

## ⚙️ Principios de POO Aplicados
El desarrollo cumple rigurosamente con los pilares de la **Programación Orientada a Objetos**:

- **Abstracción:** Uso de clases abstractas (`EntidadSistema`, `Servicio`) mediante el módulo `abc` de Python para definir plantillas obligatorias de comportamiento.  
- **Encapsulamiento:** Protección de datos sensibles del cliente (ej. `__documento`, `__nombre`) usando atributos privados y decoradores `@property` para su validación estricta.  
- **Herencia:** Implementación de clases específicas de servicios (`ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`) que heredan atributos y comportamientos de la clase base `Servicio`.  
- **Polimorfismo:** Sobrescritura de métodos clave como `calcular_costo()` y `obtener_descripcion()` en las clases derivadas para adaptar el comportamiento a cada tipo de servicio.  
- **Sobrecarga de métodos:** Implementada al estilo nativo de Python mediante argumentos por defecto (ej. el método `calcular_costo_final` acepta combinaciones dinámicas de impuestos y descuentos).  

---

## 🛡️ Manejo Avanzado de Excepciones
El sistema simula un entorno de producción donde los errores no interrumpen el flujo de la aplicación. Se implementan las siguientes estrategias:

- **Excepciones personalizadas:** Creación de una jerarquía de errores (`SoftwareFJError`, `ClienteInvalidoError`, `ReservaError`, etc.).  
- **Captura estándar:** Uso de bloques `try/except` para validaciones en tiempo real.  
- **Flujos seguros:** Bloques `try/except/else` para ejecutar código únicamente si la operación principal fue exitosa.  
- **Operaciones de limpieza:** Bloques `try/except/finally` para asegurar el cierre de procesos (ej. reportes finales o simulaciones de cierre de flujo).  
- **Encadenamiento de excepciones:** Uso de `raise ... from ...` para no perder el contexto (**Traceback**) del error original.  
- **Auditoría (Logging):** Registro automático de eventos, advertencias y errores críticos en el archivo local `sistema_logs.log`.  

---

## 🚀 Cómo ejecutar el proyecto
Sigue estos pasos para probar la simulación en tu máquina local:

1. Clona este repositorio o descarga el código fuente.  
2. Asegúrate de tener **Python 3.8 o superior** instalado en tu sistema.  
3. Abre una terminal o consola de comandos en el directorio del proyecto.  
4. Ejecuta el archivo principal con el siguiente comando:

   ```bash
   python main.py

5. Revisa la consola para ver la ejecución de la simulación de las 10 operaciones (exitosas y fallidas).
6. Verifica el archivo sistema_logs.log que se generará automáticamente en la misma carpeta para auditar los registros de ejecución.

---

## 📌 Nota
***Proyecto desarrollado para la Fase 4 del programa de Programación.***

---

