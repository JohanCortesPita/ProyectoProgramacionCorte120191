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
     #el porcentaje segun el producto
    porcentaje = coste_producto * 0.50

    #La suma del costo del producto mas el 50 porciento
    valor_producto = coste_producto + porcentaje

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
    
    #Calcula el valor trabajado por horas
    servicio = cantidad_horas * 10000
    
    return servicio

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
     #Calculado el servicio con horas extras
    
    horas_extras = cantidad_horas * 100000

    #calculamos el valor de la hora mas el calulo de la extra
    he = horas_extras + (horas_extras * 0.25)

    #valor total de la hora extra
    valor_extras = he

    return valor_extras


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
    #Calculando costo de envio fuera de la ciudad
    costo_envio = kilometros * 115

    return costo_envio

    
"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_precio_producto_fuera(coste_producto, kilometros):
    '''
    (int) -> int
    
    Calcula el valor total si el producto es por fuera de la ciudad

    >>> calcular_precio_producto_fuera(100,15)
    1875.0
    
    >>> calcular_precio_producto_fuera(15000,80)
    31700.0
    

    :param: (float) coste_producto: costo del producto
    :param: (float) kilometros: kilometros fuera de la ciudad
    :return: (float) venta_fuera_de_la_ciudad: costo total del producto fuera de la ciudad
    '''

    #calcula el precio del producto
    valor_producto = calcular_precio_producto(coste_producto)

    #Calculando costo de envio fuera de la ciudad
    costo_envio = calcular_costo_envio(kilometros)

    #Valor total de la venta fuera de la ciudad
    venta_fuera_de_la_ciudad = valor_producto + costo_envio

    return venta_fuera_de_la_ciudad

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_producto(coste_producto, tasa):
    
    '''
    #calcula el valor del iva si a la persona a la que se le vende es persona juridica
    
    >>> calcular_iva_producto(2500,19)
    712.5
    >>> calcular_iva_producto(75000,19)
    21375.0

    :param:  (float) coste_producto: costo del producto
    :param:  (float) tasa: tasa de interes
    :return: (float) valor total con iva: costo del producto con el interes
    '''
    
    #valor del producto
    valor_producto = calcular_precio_producto(coste_producto)


    #El iva del producto
    iva = valor_producto * tasa / 100

    return iva

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_servicio(cantidad_horas, tasa):
    '''
    (int) -> int
    
    calcula el iva del valor del servicio por hora
    
    >>> calcular_iva_servicio(3,19)
    57000.0
    >>> calcular_iva_servicio(24,19)
    456000.0


    :param: (float) cantidad_horas: cantidad de las hora laboradas por servicio
    :param: (float) tasa: tasa de interes
    :return: (float) servicio_con_iva: total del servico
    '''
    
    #Valores para calcular el servicio
    servicio = calcular_precio_servicio(cantidad_horas)

    #El iva del producto
    iva = servicio * tasa / 100

    return iva

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_iva_envio(kilometros, tasa):
    '''
    (int) -> int
    calcula el iva para el envio de un producto fuera de la ciudad
    
    >>> calcular_iva_envio(10,19)
    218.5
    >>> calcular_iva_envio(25,16)
    460.0

    :param kilometros: kilometros recorridos fuera de la ciudad
    :param tasa: tasa de interes
    :return: envio_con_iva: valor del iva del envio fuera de la ciudad
    '''
    #Calculando costo de envio fuera de la ciudad
    costo_envio = calcular_costo_envio(kilometros)

    #El iva del envio
    iva = costo_envio * tasa / 100

    return iva

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    '''
    (num, num) -> num
    
    >>> calcular_iva_servicio_fuera(10,16)
    160000.0
    
    :param: cantidad_horas: (int) cantidad de horas de servicio
    :param tasa: (int) tasa de interes
    :return: (float) valor del servicio con iva
    '''

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

def calcular_recaudo_locales(coste_producto_1,coste_producto_2,coste_producto_3):
     '''
    (num, num) -> num
    
    >>> calcular_recaudo_locales(1,1,1)
    4.5
    >>> calcular_recaudo_locales(60,20,30)
    165.0
    >>> calcular_recaudo_locales(20.5,15,9.5)
    67.5
    
    :param coste_producto_1: (float) coste del producto 1
    :param coste_producto_2: (float) coste del producto 2
    :param coste_producto_3: (float) coste del producto 3
    :return: (float) recaudo locales
    '''
     #Calcula el recaudo total de los productos
     return calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2) + calcular_precio_producto(coste_producto_3)

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_horas_extra(horas_1,horas_2,horas_3,horas_4):
                                 
   '''
    (num, num) -> num
    
    >>> calcular_recaudo_horas_extra(2,6,8,4)
    200000
    
    >>> calcular_recaudo_horas_extra(6,4,2,1)
    130000
    
    :param horas_1: (int) hora extra 1
    :param horas_2: (int) hora extra 2
    :param horas_3: (int) hora extra 3
    :param horas_4: (int) hora extra 4
    :return: (int) Valor del servicio (por horas extras)
    '''
   #Calcular el recaudo del total de horas extras
   return calcular_precio_servicio(horas_1) +calcular_precio_servicio(horas_2)+calcular_precio_servicio(horas_3)+calcular_precio_servicio(horas_4)

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""


def calcular_recaudo_mixto_local(coste_producto_1,coste_producto_2,horas_1,horas_2):
    """
    (num, num) -> num
    
     >>> calcular_recaudo_mixto_local(100,300,4,8)
    1200600.0
    >>> calcular_recaudo_mixto_local(5000,3500,8,8)
    1612750.0
    
    :param coste_producto_1: (num) costo del producto 1
    :param coste_producto_2: (num) costo del producto 2
    :param horas_1: (int) Horas de trabajo 1
    :param horas_2: (int) Horas de trabajo 2
    :return: (num) Recaudo mixto total
    """
    
    #Calcula el recaudo total del servicio segun las horas trabajadas
    total_horas = calcular_precio_servicio(horas_1) + calcular_precio_servicio(horas_2)

    #Calcula el recaudo total del producto segun el valor del producto
    total_productos = calcular_precio_producto(coste_producto_1) + calcular_precio_producto(coste_producto_2)


    return total_horas + total_productos
