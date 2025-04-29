import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        print(total_provincias)
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_por_provincia(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)
       
    
    def test_ventas_totales_mayores_0(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

    def test_por_provincia_inexistente(self):
        with self.assertRaises(ValueError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_por_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("Pichincha")
        self.assertIsInstance(resultado, float)
        self.assertGreaterEqual(resultado, 0)

    def test_ventas_por_provincia_3(self):
        prueba = {
            'CHIMBORAZO' : 1788637781,
            'GALAPAGOS' : 661886585,
            'MORONA SANTIAGO' : 436705038.7
        }

    def test_ventas_por_provincia_mayusculas_minusculas(self):
            """Prueba que la búsqueda no sea sensible a mayúsculas o minúsculas"""
            # Asegurarse de que "quito" y "QUITO" devuelvan el mismo resultado
            resultado_mayusculas = self.analizador.ventas_por_provincia("PICHINCHA")
            resultado_minusculas = self.analizador.ventas_por_provincia("pichincha")
            self.assertEqual(resultado_mayusculas, resultado_minusculas)
    
     
    def test_exportaciones_totales_por_mes(self):
        resultado = self.analizador.exportaciones_totales_por_mes()
        self.assertGreater(len(resultado), 0)  # Verificar que haya datos
        self.assertIn("Enero", resultado)  # Verificar si un mes específico está presente

    def test_porcentaje_ventas_tarifa_0(self):
        resultado = self.analizador.porcentaje_ventas_tarifa_0()
        self.assertGreater(len(resultado), 0)  # Verificar que haya datos
        self.assertIn("Pichincha", resultado)  # Verificar que haya una provincia específica

    def test_provincia_con_mayor_importacion(self):
        provincia, volumen = self.analizador.provincia_con_mayor_importacion()
        self.assertIsInstance(volumen, (int, float))  # Verificar que el volumen sea un número
        self.assertGreater(volumen, 0)  # Verificar que el volumen no sea 0

if __name__ == "__main__":
    unittest.main()

    