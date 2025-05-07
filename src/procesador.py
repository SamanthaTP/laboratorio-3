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

            if provincia == "ND" :
                continue

            ventas = float(fila["TOTAL_VENTAS"])
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += ventas
            else:
                ventas_por_provincia[provincia] = ventas
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre):
        total = 0
        encontrada = False
        for fila in self.datos:
            if fila["PROVINCIA"].lower() == nombre.strip().lower():
                total += fila["TOTAL_VENTAS"]
                encontrada = True
        if not encontrada:
            raise ValueError(f"La provincia '{nombre}' no se encuentra en los datos.")
        return total
    
    def exportaciones_totales_por_mes(self):
        exportaciones_por_mes = {}
        for fila in self.datos:
            mes = fila["MES"]
            exportaciones = float(fila["EXPORTACIONES"])
            if mes in exportaciones_por_mes:
                exportaciones_por_mes[mes] += exportaciones
            else:
                exportaciones_por_mes[mes] = exportaciones
        return exportaciones_por_mes

    def porcentaje_ventas_tarifa_0_por_provincia(self):
        ventas_0_por_provincia = {}
        ventas_totales_por_provincia = {}

        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            
            if provincia == "ND":
                continue

            try:
                ventas_0 = float(fila["VENTAS_NETAS_TARIFA_0"])
                total_ventas = float(fila["TOTAL_VENTAS"])
            except (KeyError, ValueError):
                continue  # omite filas con datos corruptos

            # Acumulamos las ventas tarifa 0
            if provincia in ventas_0_por_provincia:
                ventas_0_por_provincia[provincia] += ventas_0
            else:
                ventas_0_por_provincia[provincia] = ventas_0

            # Acumulamos las ventas totales
            if provincia in ventas_totales_por_provincia:
                ventas_totales_por_provincia[provincia] += total_ventas
            else:
                ventas_totales_por_provincia[provincia] = total_ventas

        # Calculamos el porcentaje
        porcentaje_por_provincia = {}
        for provincia in ventas_totales_por_provincia:
            total = ventas_totales_por_provincia[provincia]
            ventas_0 = ventas_0_por_provincia.get(provincia, 0)
            if total > 0:
                porcentaje = (ventas_0 / total) * 100
            else:
                porcentaje = 0
            porcentaje_por_provincia[provincia] = round(porcentaje, 2)

        return porcentaje_por_provincia

    # En src/procesador.py
    def diferencia_ventas_exportaciones_por_provincia(self):
        diferencia_por_provincia = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            if provincia == "ND":
                continue

            ventas = float(fila["TOTAL_VENTAS"])
            exportaciones = float(fila["EXPORTACIONES"])
            diferencia = ventas - exportaciones

            if provincia in diferencia_por_provincia:
                diferencia_por_provincia[provincia] += diferencia
            else:
                diferencia_por_provincia[provincia] = diferencia

        return diferencia_por_provincia
