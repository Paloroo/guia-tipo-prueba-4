def calcular_precio_kiosco(cant_jugo,cant_sandwich):

    precio_jugo = 500
    precio_sandwich = 300
    precio_total = (precio_sandwich * precio_jugo) + (precio_jugo * precio_sandwich)

    return precio_total

cant_san = int(input("Ingrese la cantidad de sandwiches: "))
cant_jug = int(input("Ingrese la cantidad de jugos: "))

resultado_de_la_venta = calcular_precio_kiosco(cant_san, cant_jug)
desc = round(resultado_de_la_venta * 0.10)
precio = resultado_de_la_venta * 0.90
if resultado_de_la_venta >= 5000:
    print(f"su sub total sin descuento es |{resultado_de_la_venta}| el descuentos es |{desc}| su total despues del descuento es: |{precio}|")
else:
    print("Falta comprar mas cosas.")