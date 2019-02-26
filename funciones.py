"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""
def calcular_precio_producto(coste_producto):
    """

      >>> calcular_precio_producto(1000)
    1500.0

    >>> calcular_precio_producto(500)
    750.0

    :param coste_producto:
    :return:
    """


"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_servicio(cantidad_horas):
    """
    >>> calcular_precio_servicio(1)
    100000

    >>> calcular_precio_servicio(5)
    500000

    :param cantidad_horas:
    :return:
    """


"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_servicio_extras(cantidad_horas):
    """
     >>> calcular_precio_servicio_extras(10)
    1250000.0
    >>> calcular_precio_servicio_extras(9)
    1125000.0

    :param cantidad_horas:
    :return:
    """


"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_costo_envio(kilometros):
    """
     >>> calcular_costo_envio(1)
    115
    >>> calcular_costo_envio(2)
    230

    :param kilometros:
    :return:
    """

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_precio_producto_fuera(coste_producto,kilometros):
    '''
     >>> calcular_precio_producto_fuera(100,15)
    1875.0
    >>> calcular_precio_producto_fuera(15000,80)
    31700.0
    '''
"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_producto(coste_producto, tasa):
    '''
    >>> calcular_iva_producto(2500,19)
    712.5
    >>> calcular_iva_producto(75000,19)
    21375.0
    '''
    
"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_servicio(cantidad_horas, tasa):
    '''
    >>> calcular_iva_servicio(3,19)
    57000.0
    >>> calcular_iva_servicio(24,19)
    456000.0
    '''

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_envio(kilometros, tasa):
    '''
    
    >>> calcular_iva_envio(10,19)
    218.5
    >>> calcular_iva_envio(25,16)
    460.0
    '''

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    """

    >>> calcular_iva_servicio_fuera(10,16)
    160000.0

    :param cantidad_horas:
    :param tasa:
    :return:
    """

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_locales(coste_producto_1,coste_producto_2,coste_producto_3):
   '''
    >>> calcular_recaudo_locales(1,1,1)
    4.5
    >>> calcular_recaudo_locales(60,20,30)
    165.0
    >>> calcular_recaudo_locales(20.5,15,9.5)
    67.5
    '''
"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_horas_extra(horas_1,horas_2,horas_3,horas_4):
    '''
    
    >>> calcular_recaudo_horas_extra(2,6,8,4)
    2000000
    
    >>> calcular_recaudo_horas_extra(6,4,2,1)
    1300000
    '''
"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_mixto_local(coste_producto_1,coste_producto_2,horas_1,horas_2):
    """

    >>> calcular_recaudo_mixto_local(100,300,4,8)
    1200600.0
    >>> calcular_recaudo_mixto_local(5000,3500,8,8)
    1612750.0
    :param coste_producto_1: 
    :param coste_producto_2: 
    :param horas_1: 
    :param horas_2: 
    :return: 
    """