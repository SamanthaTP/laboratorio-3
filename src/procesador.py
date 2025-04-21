import csv

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = []
        self._leer_datos()

    def _leer_datos(self):
        try:
            with open(self.archivo_csv, newline='', encoding='latin-1') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    fila["TOTAL_VENTAS"] = float(fila["TOTAL_VENTAS"])
                    self.datos.append(fila)
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo_csv} no fue encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def ventas_totales_por_provincia(self):
        ventas_por_provincia = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            ventas = fila["TOTAL_VENTAS"]
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += ventas
            else:
                ventas_por_provincia[provincia] = ventas
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre):
        total = 0
        for fila in self.datos:
            if fila["PROVINCIA"].lower() == nombre.lower():
                total += fila["TOTAL_VENTAS"]
        return total
