
# 🧮 Analizador de Datos Económicos por Provincia

Este proyecto en Python analiza datos económicos (ventas, exportaciones e importaciones) por provincia en Ecuador, con el fin de generar reportes útiles y automatizados a partir de archivos CSV.

## 📁 Estructura del Proyecto

```
.
├── app.py                    # Script principal para ejecutar el análisis
├── src/
│   └── procesador.py         # Contiene la lógica de procesamiento y análisis de datos
├── tests/
│   └── test_analizador.py    # Pruebas unitarias
├── data/
│   └── datos.csv             # Archivo de datos de entrada (ventas, exportaciones, etc.)
└── README.md                 # Este archivo
```

## 🚀 ¿Cómo ejecutar el proyecto?

1. Asegúrate de tener Python instalado (recomendado: 3.8+).
2. Coloca tu archivo de datos en la carpeta `data/` con nombre `datos.csv`.
3. Ejecuta el archivo principal:

```bash
python app.py
```

## ✅ Funcionalidades principales

- Total de exportaciones por mes.
- Total de ventas por provincia.
- Porcentaje de ventas con tarifa 0% por provincia.
- Provincia con mayor volumen de importaciones.
- Filtrado y manejo de datos faltantes (como “ND”).

## 🧪 Pruebas

El proyecto incluye pruebas unitarias con `unittest`.

Para ejecutarlas:

```bash
python -m unittest discover tests
```

## 📌 Requisitos

- Python 3.8 o superior
- Archivo CSV estructurado con columnas:
  - `PROVINCIA`
  - `TOTAL_VENTAS`
  - `VENTAS_NETAS_TARIFA_0`
  - `IMPORTACIONES`
  - `EXPORTACIONES`
  - `MES`

## ✨ Ejemplo de salida

```bash
Exportaciones totales por mes:
    Enero: $12,000.50
    Febrero: $13,600.00
...

Porcentaje de ventas con tarifa 0% por provincia:
    Pichincha: 27.5%
    Guayas: 19.3%
...

Provincia con mayor volumen de importaciones:
    Guayas con $98,765.43
```

## 📄 Licencia

Este proyecto es de libre uso con fines educativos.

## 🙌 Autor

Proyecto desarrollado por [Tu Nombre Aquí].
