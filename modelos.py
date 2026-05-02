"""
Módulo de Modelos de Negocio (modelos.py)
-----------------------------------------
Contiene las entidades principales del sistema aplicando rigurosamente los 
pilares de la POO: Abstracción, Herencia, Polimorfismo y Encapsulamiento.
"""

import logging
from abc import ABC, abstractmethod
from datetime import datetime
from excepciones import ClienteInvalidoError, ReservaError, ServicioNoDisponibleError

# ==========================================
# 1. ABSTRACCIÓN (Clases Base)
# ==========================================
class EntidadSistema(ABC):
    """
    Clase abstracta superior. Representa cualquier entidad que exista en el sistema.
    Hereda de ABC (Abstract Base Class) para evitar que sea instanciada directamente.
    """
    def __init__(self):
        # Toda entidad creada registrará automáticamente la fecha y hora de su creación
        self.fecha_creacion = datetime.now()
        
    @abstractmethod
    def obtener_identificador(self) -> str:
        """
        Método abstracto puro. Obliga a TODAS las clases hijas a implementar 
        su propia forma de devolver un ID único (ej. cédula para cliente, código para servicio).
        """
        pass

class Servicio(EntidadSistema):
    """
    Clase abstracta intermedia para los servicios ofrecidos por la empresa.
    Hereda de EntidadSistema y define atributos comunes para cualquier servicio.
    """
    def __init__(self, id_servicio: str, nombre: str, precio_base: float):
        super().__init__() # Llama al constructor de EntidadSistema
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = True # Todos los servicios nacen estando disponibles

    def obtener_identificador(self) -> str:
        # Implementación del método abstracto de EntidadSistema
        return self.id_servicio

    @abstractmethod
    def calcular_costo(self, duracion_horas: int) -> float:
        """
        Método polimórfico abstracto. Cada tipo de servicio calculará 
        su costo de forma diferente dependiendo de sus reglas de negocio.
        """
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Método polimórfico para obtener los detalles específicos del servicio."""
        pass

# ==========================================
# 2. HERENCIA Y POLIMORFISMO (Clases Derivadas)
# ==========================================
class ReservaSala(Servicio):
    """Clase derivada específica para reservar salas físicas."""
    def __init__(self, id_servicio: str, nombre: str, precio_base: float, capacidad: int):
        super().__init__(id_servicio, nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, duracion_horas: int) -> float:
        # Polimorfismo: Si la sala se reserva por más de 5 horas, se aplica un 10% de descuento.
        costo = self.precio_base * duracion_horas
        if duracion_horas > 5:
            costo *= 0.90 
        return costo

    def obtener_descripcion(self) -> str:
        return f"Sala '{self.nombre}' (Capacidad: {self.capacidad} pers)."

class AlquilerEquipo(Servicio):
    """Clase derivada para el alquiler de hardware o maquinaria."""
    def __init__(self, id_servicio: str, nombre: str, precio_base: float, requiere_seguro: bool):
        super().__init__(id_servicio, nombre, precio_base)
        self.requiere_seguro = requiere_seguro

    def calcular_costo(self, duracion_horas: int) -> float:
        # Polimorfismo: Se cobra un cargo fijo adicional de 50.0 si el equipo exige seguro.
        costo = self.precio_base * duracion_horas
        if self.requiere_seguro:
            costo += 50.0 
        return costo

    def obtener_descripcion(self) -> str:
        seguro = "con seguro" if self.requiere_seguro else "sin seguro"
        return f"Equipo '{self.nombre}' ({seguro})."

class AsesoriaEspecializada(Servicio):
    """Clase derivada para la contratación de horas profesionales."""
    def __init__(self, id_servicio: str, nombre: str, precio_base: float, experto: str):
        super().__init__(id_servicio, nombre, precio_base)
        self.experto = experto

    def calcular_costo(self, duracion_horas: int) -> float:
        # Polimorfismo: Si la asesoría dura más de 2 horas, las horas totales 
        # sufren un recargo del 20% por concepto de desgaste o especialidad.
        if duracion_horas > 2:
            return (self.precio_base * 1.20) * duracion_horas
        return self.precio_base * duracion_horas

    def obtener_descripcion(self) -> str:
        return f"Asesoría '{self.nombre}' dictada por {self.experto}."

# ==========================================
# 3. ENCAPSULAMIENTO ESTRICTO
# ==========================================
class Cliente(EntidadSistema):
    """Representa a un cliente del sistema aplicando protección de datos (encapsulamiento)."""
    def __init__(self, documento: str, nombre: str, correo: str):
        super().__init__()
        # Se declaran atributos privados (precedidos por __)
        self.__documento = None
        self.__nombre = None
        self.__correo = None
        
        # Bloque Try/Except con Encadenamiento de Excepciones:
        # Intentamos asignar los valores usando las properties (que tienen validaciones).
        # Si un setter lanza un ValueError, lo atrapamos y lanzamos nuestro error personalizado,
        # encadenando (from e) el error original para no perder el contexto.
        try:
            self.documento = documento
            self.nombre = nombre
            self.correo = correo
        except ValueError as e:
            raise ClienteInvalidoError(f"Error al crear cliente: {e}") from e

    def obtener_identificador(self) -> str:
        return self.__documento

    # Propiedades (Properties): Actúan como Getters y Setters seguros
    @property
    def documento(self): 
        return self.__documento

    @documento.setter
    def documento(self, valor: str):
        # Validación: El documento no puede estar vacío y debe ser alfanumérico
        if not valor or not valor.isalnum():
            raise ValueError("El documento debe ser alfanumérico.")
        self.__documento = valor

    @property
    def nombre(self): 
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        # Validación: El nombre debe tener al menos 3 caracteres
        if not valor or len(valor) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor

    @property
    def correo(self): 
        return self.__correo

    @correo.setter
    def correo(self, valor: str):
        # Validación básica de estructura de correo electrónico
        if "@" not in valor or "." not in valor:
            raise ValueError("Formato de correo electrónico inválido.")
        self.__correo = valor

# ==========================================
# 4. COMPOSICIÓN Y LÓGICA TRANSACCIONAL
# ==========================================
class Reserva(EntidadSistema):
    """
    Integra clientes, servicios y el estado de la transacción.
    Maneja la lógica de negocio central de las confirmaciones.
    """
    _contador_reservas = 1 # Atributo de clase (estático) para generar IDs autoincrementales

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: int):
        super().__init__()
        # Formateo del ID autoincremental, ej. RES-0001
        self.id_reserva = f"RES-{Reserva._contador_reservas:04d}"
        Reserva._contador_reservas += 1
        
        # Agregación: La reserva guarda referencias al cliente y al servicio
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente" # Estado inicial por defecto
        
        # Validación de negocio
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0 horas.")
        self.duracion = duracion

    def obtener_identificador(self) -> str:
        return self.id_reserva

    def calcular_costo_final(self, impuesto: float = 0.0, descuento_adicional: float = 0.0) -> float:
        """
        Simulación de Sobrecarga de Métodos.
        En Python, esto se logra usando argumentos por defecto. Este método puede llamarse:
        - sin argumentos: calcular_costo_final()
        - con 1 argumento: calcular_costo_final(impuesto=0.19)
        - con 2 argumentos: calcular_costo_final(0.19, 0.05)
        """
        # Se invoca el método polimórfico calcular_costo del servicio correspondiente
        costo_base = self.servicio.calcular_costo(self.duracion)
        costo_con_descuento = costo_base - (costo_base * descuento_adicional)
        return costo_con_descuento + (costo_con_descuento * impuesto)

    def confirmar(self):
        """
        Cambia el estado de la reserva a Confirmada, pero realiza 
        validaciones críticas que pueden levantar excepciones.
        """
        if not self.servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.servicio.nombre} no está disponible.")
        if self.estado == "Cancelada":
            raise ReservaError("Reserva ya cancelada.")
        
        self.estado = "Confirmada"

    def cancelar(self):
        """Cancela la reserva, marcándola inactiva."""
        self.estado = "Cancelada"
