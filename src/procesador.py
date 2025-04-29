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

            ventas = fila["TOTAL_VENTAS"]
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
            exportaciones = fila["EXPORTACIONES"]
            if mes in exportaciones_por_mes:
                exportaciones_por_mes[mes] += exportaciones
            else:
                exportaciones_por_mes[mes] = exportaciones
        return exportaciones_por_mes
    
    def porcentaje_ventas_tarifa_0(self):
        porcentaje_por_provincia = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            ventas_netas_tarifa_0 = fila["VENTAS_NETAS_TARIFA_0"]
            total_ventas = fila["TOTAL_VENTAS"]
        
        if total_ventas == 0:  # Para evitar la división por 0
            porcentaje = 0
        else:
            porcentaje = (ventas_netas_tarifa_0 / total_ventas) * 100
        
        if provincia in porcentaje_por_provincia:
            porcentaje_por_provincia[provincia].append(porcentaje)
        else:
            porcentaje_por_provincia[provincia] = [porcentaje]
    
        # Promedio por provincia
        promedio_por_provincia = {prov: sum(valores) / len(valores) for prov, valores in porcentaje_por_provincia.items()}
        return promedio_por_provincia
    
    def provincia_con_mayor_importacion(self):
        importaciones_por_provincia = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"]
            importaciones = fila["IMPORTACIONES"]
        
            if provincia in importaciones_por_provincia:
                importaciones_por_provincia[provincia] += importaciones
            else:
                importaciones_por_provincia[provincia] = importaciones
    
        # Encontrar la provincia con mayor volumen de importaciones
        provincia_maxima = max(importaciones_por_provincia, key=importaciones_por_provincia.get)
        return provincia_maxima, importaciones_por_provincia[provincia_maxima]


