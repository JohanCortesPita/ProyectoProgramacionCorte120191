"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""
def calcular_precio_producto(coste_producto):
    '''
    (int) -> int
    
    Calcula el costo de un producto mas el 50%
    
    >>> calcular_precio_producto(1000)
    1500.0
    >>> calcular_precio_producto(500)
    750.0
    
    :param coste_producto: (int) valor del producto
    :return: (int) Valor total del producto
    '''

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_servicio(cantidad_horas):
    '''
    (int) -> (int)
    
    Calcula el valor total del servicio segun horas trabajadas
    
    >>> calcular_precio_servicio(1)
    100000
    >>> calcular_precio_servicio(5)
    500000

    :param cantidad_horas: int Horas trabajadas
    :return: int Valor total del servicio segun horas trabajadas
    '''

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_servicio_extras(cantidad_horas):
    '''
    (int) -> int
    Calcula el total de horas trabajadas y define el total de la tarifa mas horas extras
    
     >>> calcular_precio_servicio_extras(10)
    1250000.0
    >>> calcular_precio_servicio_extras(9)
    1125000.0
    
    :param cantidad_horas: int Horas trabajadas
    :return: int Tarifa total del servicio con horas extras
    '''


"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_costo_envio(kilometros):
    '''
    (int) -> int
    Calcula el total de kilometros recorridos fuera de la ciudad y define el total del envio del costo
    
    >>> calcular_costo_envio(1)
    115
    >>> calcular_costo_envio(2)
    230

    :param kilometros: Kilometros recorridos
    :return: Valor del envio
    '''
    
"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    """
    
    (int) -> int
    
    Calcula el valor total si el producto es por fuera de la ciudad

    :param: (float) coste_producto: costo del producto
    :param: (float) kilometros: kilometros fuera de la ciudad
    :return: (float) venta_fuera_de_la_ciudad: costo total del producto fuera de la ciudad
    """

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_producto(coste_producto, tasa):
    
    '''
    calcula el valor del iva si a la persona a la que se le vende es persona juridica


    :param:  (float) coste_producto: costo del producto
    :param:  (float) tasa: tasa de interes
    :return: (float) valor total con iva: costo del producto con el interes
    '''

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_servicio(cantidad_horas, tasa):
    '''
    (int) -> int
    
    calcula el iva del valor del servicio por hora


    :param: (float) cantidad_horas: cantidad de las hora laboradas por servicio
    :param: (float) tasa: tasa de interes
    :return: (float) servicio_con_iva: total del servico
    '''

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_envio(kilometros, tasa):
    '''
    (int) -> int
    calcula el iva para el envio de un producto fuera de la ciudad


    :param kilometros: kilometros recorridos fuera de la ciudad
    :param tasa: tasa de interes
    :return: envio_con_iva: valor del iva del envio fuera de la ciudad
    '''

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_iva_servicio_fuera(cantidad_horas, tasa):

#Calcula el precio del servicio segun la cantidad de horas
    servicio = calcular_precio_servicio(cantidad_horas)

    #Iva del servicio fuera de la cuidad
    iva = servicio * tasa / 100

    return iva

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):


     # Calcula el recaudo total de los productos
    return calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2) + calcular_precio_producto(coste_producto_3)

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
   #Calcular el recaudo del total de horas extras
    return calcular_precio_servicio(horas_1) +calcular_precio_servicio(horas_2)+calcular_precio_servicio(horas_3)+calcular_precio_servicio(horas_4)

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    """

    :param coste_producto_1:
    :param coste_producto_2:
    :param horas_1:
    :param horas_2:
    :return:
    """

    #Calcula el recaudo total del servicio segun las horas trabajadas
    total_horas = calcular_precio_servicio(horas_1) + calcular_precio_servicio(horas_2)

    #Calcula el recaudo total del producto segun el valor del producto
    total_productos = calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2)

    return total_horas + total_productos
