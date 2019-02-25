import unittest
import funciones as f
# Pruebas -> Casos extremos
#            2 Pruebas flujo normal

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(0), 0)
        self.assertEqual(f.calcular_precio_producto(500), 750)
        self.assertEqual(f.calcular_precio_producto(-100), 'El valor debe ser mayor que 0')
        self.assertEqual(f.calcular_precio_producto(-50), 'El valor debe ser mayor que 0' )

    def test_calcular_precio_servicio(self):
        self.assertEqual(f.calcular_precio_servicio(1), 100000)
        self.assertEqual(f.calcular_precio_servicio(5), 500000)
        self.assertEqual(f.calcular_precio_servicio(0), 0)
        self.assertEqual(f.calcular_precio_servicio(-1), 'Las horas trabajadas deben ser mayores de 0')
        self.assertEqual(f.calcular_precio_servicio(-5), 'Las horas trabajadas deben ser mayores de 0')

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(f.calcular_precio_servicio_extras(10), 1250000)
        self.assertEqual(f.calcular_precio_servicio_extras(9), 1125000)
        self.assertEqual(f.calcular_precio_servicio_extras(1), 125000)
        self.assertEqual(f.calcular_precio_servicio_extras(0), 0)
        self.assertEqual(f.calcular_precio_servicio_extras(-1), 'La horas trabajadas deben ser mayores a 0')
        self.assertEqual(f.calcular_precio_servicio_extras(-5), 'La horas trabajadas deben ser mayores a 0')

    def test_calcular_costo_envio(self):
        self.assertEqual(f.calcular_costo_envio(1), 115)
        self.assertEqual(f.calcular_costo_envio(2), 230)
        self.assertEqual(f.calcular_costo_envio(0), 0)
        self.assertIsNot(f.calcular_costo_envio(-1), 'No es valido')
        self.assertIsNot(f.calcular_costo_envio(-2), 'No es valido')


    def test_calcular_precio_producto_fuera(self):
        pass

    def test_calcular_iva_producto(self):
        pass

    def test_calcular_iva_servicio(self):
        pass

    def test_calcular_iva_envio(self):
        pass

    def test_calcular_iva_servicio_fuera(self):
        pass

    def test_calcular_recaudo_locales(self):
        pass

    def test_calcular_recaudo_horas_extra(self):
        pass

    def test_calcular_recaudo_mixto_local(self):
        pass


if __name__ == 'main':
    unittest.main()
