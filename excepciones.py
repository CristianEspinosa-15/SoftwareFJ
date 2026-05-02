"""
Módulo de Excepciones Personalizadas (excepciones.py)
------------------------------------------------------
Este módulo centraliza todas las excepciones específicas del dominio de Software FJ.
Al heredar de la clase base Exception, creamos errores semánticos que hacen 
que el código principal sea más legible y fácil de depurar.
"""

class SoftwareFJError(Exception):
    """
    Clase base fundamental para todas las excepciones de nuestro sistema.
    Cualquier error específico de la aplicación heredará de esta clase.
    Esto permite capturar cualquier error de negocio usando un solo 'except SoftwareFJError'.
    """
    pass

class ClienteInvalidoError(SoftwareFJError):
    """
    Excepción lanzada específicamente cuando la validación de los datos 
    de un cliente (documento, nombre, correo) falla en los métodos 'setter'.
    """
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """
    Excepción lanzada cuando un usuario o el sistema intenta confirmar 
    una reserva sobre un servicio que temporalmente no está habilitado 
    (disponible = False).
    """
    pass

class ReservaError(SoftwareFJError):
    """
    Excepción lanzada cuando ocurre una inconsistencia en la lógica de negocio 
    de una reserva, como por ejemplo: duraciones negativas, o intentar confirmar 
    una reserva que ya había sido cancelada previamente.
    """
    pass
