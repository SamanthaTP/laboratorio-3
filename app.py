from src.procesador import Analizador

def main():
    archivo = "data/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:.2f}")

    print("\nCompras para una provincia")
    try:
        provincia = input("\tIngrese el nombre de una provincia: ")
        ventas = analizador.ventas_por_provincia(provincia)
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    except ValueError as e:
        print(e)


    print("Exportaciones totales por mes:")
    resumen = analizador.exportaciones_totales_por_mes()
    for mes, total in resumen.items():
        print(f"\t{mes}: ${total:,.2f}")

    print("\nPorcentaje de ventas con tarifa 0% por provincia:")
    porcentaje_tarifa_0 = analizador.porcentaje_ventas_tarifa_0_por_provincia()
    for prov, porcentaje in porcentaje_tarifa_0.items():
        print(f"\t{prov}: {porcentaje:.2f}%")


if __name__ == "__main__":
    main()
