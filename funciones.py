"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_producto(coste_producto):
    '''
    (int) -> int
    Calcula el costo de un producto mas el 50%



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



    :param kilometros: Kilometros recorridos
    :return: Valor del envio
    '''


"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_precio_producto_fuera(coste_producto,kilometros):
    """
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
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""

def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    pass
