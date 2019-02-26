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
        self.assertEqual(f.calcular_precio_producto_fuera(5000,100),19000)
        self.assertEqual(f.calcular_precio_producto_fuera(2000, 100), 14500

    def test_calcular_iva_producto(self):
        self.assertEqual(f.calcular_iva_producto(5000,7),525)
        self.assertEqual(f.calcular_iva_producto(5000,0), "El producto no tiene iva")
        self.assertEqual(f.calcular_iva_producto(5000,-1), "Verifique Iva")

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(5, 14),7000)
        self.assertIsNot(f.calcular_iva_servicio(0, 14), "No realizo horas de servicio")
        self.assertIsNot(f.calcular_iva_servicio(-1, 14), "Revisar las horas ingresadas")

    
    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_envio(20, 16), 368.0)
        self.assertIsNot(f.calcular_iva_envio(5, 0), "No aplica iva")
        self.assertIsNot(f.calcular_iva_envio(-17, 16), "cifra no valida")

    def test_calcular_iva_servicio_fuera(self):
        self.assertEqual(f.calcular_iva_servicio_fuera(10,16),160000.0)
        self.assertEqual(f.calcular_iva_servicio_fuera(-4,-48),"Cifras no validas")
        self.assertEqual(f.calcular_iva_servicio_fuera(-8,98),"Cifras no validas")
        self.assertEqual(f.calcular_iva_servicio_fuera(-8,89),"Cifras no validas")

    def test_calcular_recaudo_locales(self):
        self.assertEqual(f.calcular_recaudo_locales(1,1,1),4.5)
        self.assertEqual(f.calcular_recaudo_locales(60,20,30),165.0)
        self.assertEqual(f.calcular_recaudo_locales(20.5,15,9.5),67.5)
        self.assertEqual(f.calcular_recaudo_locales(20.89,854,-85),"Cifras no validas")

    def test_calcular_recaudo_horas_extra(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(2,6,8,4),200000)
        self.assertEqual(f.calcular_recaudo_horas_extra(6,4,2,1),130000)
        self.assertEqual(f.calcular_recaudo_horas_extra(5,4,3,-85),"Cifras no validas")
        self.assertEqual(f.calcular_recaudo_horas_extra(-5,-54,-98,-68),"Cifras no vlidas")


    def test_calcular_recaudo_mixto_local(self):
        self.assertEqual(f.calcular_recaudo_mixto_local(100,300,4,8),1200600.0)
        self.assertEqual(f.calcular_recaudo_mixto_local(5000,3500,8,8),1612750.0)
        self.assertEqual(f.calcular_recaudo_mixto_local(-100,50,-85,58),"Cifras no validas")
        self.assertEqual(f.calcular_recaudo_mixto_local(5,98,4,8),"Cifras no validas")


if __name__ == 'main':
    unittest.main()
