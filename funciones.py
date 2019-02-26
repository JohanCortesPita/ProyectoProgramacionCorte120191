"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""
def calcular_precio_producto(coste_producto):
    precio_producto=((coste_producto/2)+(coste_producto))
    return precio_producto

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_servicio(cantidad_horas):
    precio_servicio= (cantidad_horas*10000)
    return precio_servicio

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_precio_servicio_extras(cantidad_horas):
    pass

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_costo_envio(kilometros):

    pass


"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):

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
