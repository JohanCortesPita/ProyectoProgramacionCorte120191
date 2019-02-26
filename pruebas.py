import unittest
import funciones as f
# Pruebas -> Casos extremos
#            2 Pruebas flujo normal

class pruebas(unittest.TestCase):

    """
    Desarrollo: Edward
    Pruebas: Johan
    Documentación: David
    """
    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(0), 0)

    """
    Desarrollo: Edward
    Pruebas: Johan
    Documentación: David
    """
    def test_calcular_precio_servicio(self):
        pass

    """
    Desarrollo: Edward
    Pruebas: Johan
    Documentación: David
    """
    def test_calcular_precio_servicio_extras(self):
        pass

    """
    Desarrollo: Edward
    Pruebas: Johan
    Documentación: David
    """
    def test_calcular_costo_envio(self):
        pass

    """
    Desarrollo: David
    Pruebas: Edward
    Documentación: Johan
    """
    def test_calcular_precio_producto_fuera(self):
        pass

    """
    Desarrollo: David
    Pruebas: Edward
    Documentación: Johan
    """
    def test_calcular_iva_producto(self):
        pass

    """
    Desarrollo: David
    Pruebas: Edward
    Documentación: Johan
    """
    def test_calcular_iva_servicio(self):
        pass

    """
    Desarrollo: David
    Pruebas: Edward
    Documentación: Johan
    """
    def test_calcular_iva_envio(self):
        pass

    """
    Desarrollo: Johan
    Pruebas: David
    Documentación: Edward
    """
    def test_calcular_iva_servicio_fuera(self):
        self.assertEqual(f.calcular_iva_servicio_fuera(10,16),160000.0)
        self.assertEqual(f.calcular_iva_servicio_fuera(-4,-48),"Cifras no validas")
        self.assertEqual(f.calcular_iva_servicio_fuera(-8,98),"Cifras no validas")
        self.assertEqual(f.calcular_iva_servicio_fuera(-8,89),"Cifras no validas")

    """
    Desarrollo: Johan
    Pruebas: David
    Documentación: Edward
    """
    def test_calcular_recaudo_locales(self):
        self.assertEqual(f.calcular_recaudo_locales(1,1,1),4.5)
        self.assertEqual(f.calcular_recaudo_locales(60,20,30),165.0)
        self.assertEqual(f.calcular_recaudo_locales(20.5,15,9.5),67.5)
        self.assertEqual(f.calcular_recaudo_locales(20.89,854,-85),"Cifras no validas")

    """
    Desarrollo: Johan
    Pruebas: David
    Documentación: Edward
    """
    def test_calcular_recaudo_horas_extra(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(2,6,8,4),2000000)
        self.assertEqual(f.calcular_recaudo_horas_extra(6,4,2,1),1300000)
        self.assertEqual(f.calcular_recaudo_horas_extra(5,4,3,-85),"Cifras no validas")
        self.assertEqual(f.calcular_recaudo_horas_extra(-5,-54,-98,-68),"Cifras no vlidas")

    """
    Desarrollo: Johan
    Pruebas: David
    Documentación: Edward
    """
    def test_calcular_recaudo_mixto_local(self):
        self.assertEqual(f.calcular_recaudo_mixto_local(100,300,4,8),1200600.0)
        self.assertEqual(f.calcular_recaudo_mixto_local(5000,3500,8,8),1612750.0)
        self.assertEqual(f.calcular_recaudo_mixto_local(-100,50,-85,58),"Cifras no validas")
        self.assertEqual(f.calcular_recaudo_mixto_local(5,98,4,8),"Cifras no validas")

if __name__ == 'main':
    unittest.main()
