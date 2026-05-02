"""
Módulo Controlador del Sistema (sistema.py)
-------------------------------------------
Actúa como la base de datos en memoria y coordina la lógica de la aplicación.
Ejecuta las 10 operaciones de simulación requeridas, demostrando diferentes 
formas de capturar y manejar excepciones y registrar logs.
"""

import logging
from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada, Reserva
from excepciones import ClienteInvalidoError, ReservaError, ServicioNoDisponibleError

# Configuración central del sistema de Logging.
# Todo evento importante se escribirá en el archivo 'sistema_logs.log' sin detener la app.
logging.basicConfig(
    filename='sistema_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class SistemaGestion:
    """Clase principal que simula el almacenamiento y ejecución del sistema."""
    
    def __init__(self):
        # Simulamos una base de datos utilizando listas en memoria RAM
        self.clientes = []
        self.servicios = []
        self.reservas = []
        
        # Lista temporal para guardar los textos que se mostrarán en la interfaz gráfica
        self.salida_texto = [] 

    def registrar_mensaje(self, mensaje):
        """Método auxiliar que guarda mensajes para la GUI y los imprime en consola oculta."""
        self.salida_texto.append(mensaje)
        print(mensaje)

    def obtener_historial_simulacion(self):
        """Une toda la salida acumulada en un solo texto para la interfaz."""
        return "\n".join(self.salida_texto)

    def limpiar_historial(self):
        """Limpia el buffer de la interfaz antes de iniciar una nueva simulación."""
        self.salida_texto = []

    def ejecutar_simulacion(self):
        """
        Método núcleo. Ejecuta las 10 operaciones solicitadas en la guía, 
        aplicando estructuras try/except avanzadas para garantizar estabilidad.
        """
        self.limpiar_historial()
        self.registrar_mensaje("--- INICIANDO SIMULACIÓN 10 OPERACIONES ---")
        logging.info("Inicio de simulación mediante GUI")

        # Operación 1: Instanciación correcta
        self.registrar_mensaje("\n[Op 1] Creando cliente válido...")
        try:
            c1 = Cliente("1001", "Carlos Perez", "carlos@mail.com")
            self.clientes.append(c1)
            self.registrar_mensaje(f"✅ Éxito: Cliente {c1.nombre} creado.")
            logging.info("Cliente creado exitosamente: Carlos Perez")
        except Exception as e:
            self.registrar_mensaje(f"❌ Fallo inesperado: {e}")

        # Operación 2: Falla intencional en setter (correo inválido)
        self.registrar_mensaje("\n[Op 2] Creando cliente con correo inválido...")
        try:
            # Falta el símbolo @
            c_malo = Cliente("1002", "Ana", "correo_sin_arroba.com")
        except ClienteInvalidoError as e:
            # Captura la excepción personalizada y registra el error formalmente en los logs
            logging.error(f"Op 2 fallida (Dato inválido): {e}")
            self.registrar_mensaje(f"✅ Error capturado (Esperado): {e}")

        # Operación 3: Falla intencional en setter (nombre muy corto)
        self.registrar_mensaje("\n[Op 3] Creando cliente con nombre corto...")
        try:
            # 'Al' tiene menos de 3 caracteres
            c_malo2 = Cliente("1003", "Al", "al@mail.com")
        except ClienteInvalidoError as e:
            logging.error(f"Op 3 fallida (Parámetro inválido): {e}")
            self.registrar_mensaje(f"✅ Error capturado (Esperado): {e}")

        # Operación 4: Instanciación de herencia y polimorfismo
        self.registrar_mensaje("\n[Op 4] Registrando servicios...")
        # Creamos instancias de las 3 clases derivadas distintas
        s1 = ReservaSala("S01", "Sala VIP", 100.0, 15)
        s2 = AlquilerEquipo("E01", "Proyector 4K", 20.0, requiere_seguro=True)
        s3 = AsesoriaEspecializada("A01", "Arquitectura Cloud", 150.0, "Ing. Gomez")
        self.servicios.extend([s1, s2, s3])
        
        # Demostramos polimorfismo llamando a obtener_descripcion() sin importar de qué clase hija sea
        for s in self.servicios:
            self.registrar_mensaje(f"  -> Registrado: {s.obtener_descripcion()}")

        # Operación 5: Uso de try/except/else
        self.registrar_mensaje("\n[Op 5] Creando reserva exitosa (Try/Except/Else)...")
        try:
            # Se intenta crear una reserva válida de 6 horas
            reserva1 = Reserva(self.clientes[0], self.servicios[0], 6)
        except ReservaError as e:
            # Si falla, se atrapa aquí
            self.registrar_mensaje(f"❌ Error: {e}")
        else:
            # Este bloque ELSE SOLO SE EJECUTA si el try no lanzó ninguna excepción.
            # Es el lugar ideal para guardar datos definitivos.
            self.reservas.append(reserva1)
            self.registrar_mensaje(f"✅ Reserva creada: {reserva1.id_reserva}")
            self.registrar_mensaje(f"   Costo sin impuestos: ${reserva1.calcular_costo_final():.2f}")

        # Operación 6: Confirmación de reserva
        self.registrar_mensaje("\n[Op 6] Confirmando reserva...")
        try:
            self.reservas[0].confirmar()
            self.registrar_mensaje(f"✅ Estado de la reserva: {self.reservas[0].estado}")
            logging.info(f"Reserva {self.reservas[0].id_reserva} confirmada")
        except Exception as e:
            self.registrar_mensaje(f"❌ Error al confirmar: {e}")

        # Operación 7: Validaciones de lógica interna (duración inválida)
        self.registrar_mensaje("\n[Op 7] Creando reserva con duración negativa...")
        try:
            # -2 horas no tiene sentido físico
            reserva_mala = Reserva(self.clientes[0], self.servicios[1], -2)
        except ReservaError as e:
            logging.warning(f"Intento de reserva con parámetros absurdos: {e}")
            self.registrar_mensaje(f"✅ Excepción controlada (Esperada): {e}")

        # Operación 8: Validación de estado (Servicio no disponible)
        self.registrar_mensaje("\n[Op 8] Confirmando reserva de servicio deshabilitado...")
        try:
            # Modificamos el estado para forzar el fallo
            self.servicios[2].disponible = False
            reserva2 = Reserva(self.clientes[0], self.servicios[2], 3)
            # Intentamos confirmar sabiendo que lanzará un error
            reserva2.confirmar()
        except ServicioNoDisponibleError as e:
            logging.error(f"Error de disponibilidad en confirmación: {e}")
            self.registrar_mensaje(f"✅ Error capturado (Esperado): {e}")

        # Operación 9: Uso de try/except/finally
        self.registrar_mensaje("\n[Op 9] Error matemático crítico (Try/Except/Finally)...")
        try:
            # Forzamos una división matemática inválida
            total_clientes = len(self.clientes) - 1 # Restamos 1 a propósito para que dé 0
            promedio = 1000 / total_clientes
        except ZeroDivisionError as e:
            logging.critical("Cálculo inconsistente: División por cero evitada.")
            self.registrar_mensaje("✅ Error matemático controlado: División por cero evitada.")
        finally:
            # Este bloque FINALLY SE EJECUTA SIEMPRE, haya existido error o no.
            # Es vital para cerrar conexiones a BD, archivos, o liberar memoria en un sistema real.
            self.registrar_mensaje("✅ Bloque Finally: Simulando liberación de recursos del sistema...")

        # Operación 10: Demostración de métodos sobrecargados (argumentos dinámicos)
        self.registrar_mensaje("\n[Op 10] Sobrecarga de método (Costos con variaciones)...")
        if self.reservas:
            r = self.reservas[0]
            # Varias llamadas al mismo método pero con distintas configuraciones de parámetros
            self.registrar_mensaje(f"  Base (Sin params): ${r.calcular_costo_final():.2f}")
            self.registrar_mensaje(f"  Con Impuesto 19% (1 param): ${r.calcular_costo_final(impuesto=0.19):.2f}")
            self.registrar_mensaje(f"  Ambos (Imp 19% + Dcto 5%) (2 params): ${r.calcular_costo_final(impuesto=0.19, descuento_adicional=0.05):.2f}")

        self.registrar_mensaje("\n--- SIMULACIÓN FINALIZADA SIN INTERRUPCIONES ---")
