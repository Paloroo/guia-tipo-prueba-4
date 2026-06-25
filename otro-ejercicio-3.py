def mostrar_menu():
    print("\n---  CAFETÍN ULTRA RÁPIDO ---")
    print("1. Agregar un pedido")
    print("2. Buscar un pedido")
    print("3. Eliminar un pedido")
    print("4. Actualizar estados (Truco mágico)")
    print("5. Mostrar todos los pedidos")
    print("6. Salir")

def agregar_pedido():
    print("\n--- NUEVO PEDIDO ---")
    producto = input("¿Qué producto quieres? (Ej: Cafe): ")
    
    try:
        cantidad = int(input("¿Cuántos quieres? (1 al 20): "))
        if cantidad < 1 or cantidad > 20:
            print("¡Oye! Solo se permiten entre 1 y 20.")
            return 

        precio_unitario = float(input("¿Cuánto cuesta cada uno?: $"))
        if precio_unitario <= 0:
            print("¡El precio debe ser mayor a 0!")
            return
            
    except ValueError:
        print("¡ERROR! Tenías que escribir un número, no letras.")
        return

    total = cantidad * precio_unitario

    nuevo_pedido = {
        "producto": producto,
        "cantidad": cantidad,
        "total": total,
        "despacho_rapido": False
    }
    pedido = nuevo_pedido
    pedido.append(nuevo_pedido)
    print("¡Pedido guardado con éxito!")

# 4. Función para buscar un pedido por su nombre exacto
def buscar_pedido():
    print("\n--- BUSCADOR ---")
    buscado = input("¿Qué producto buscas?: ")
    encontrado = False
    
    pedidos = buscar_pedido

    for p in pedidos:
        if p["producto"] == buscado:
            print(f"🎯 ¡Encontrado! -> {p['producto']} | Cantidad: {p['cantidad']} | Total: ${p['total']}")
            encontrado = True
    
    if not encontrado:
        print("No encontramos ningún pedido con ese nombre.")

# 5. Función para borrar un pedido de la lista
def eliminar_pedido():
    print("\n--- BORRADOR ---")
    borrar = input("¿Qué producto quieres eliminar?: ")
    pedidos = buscar_pedido
    for p in pedidos:
        if p["producto"] == borrar:
            pedidos.remove(p)
            print("🗑️ ¡Pedido eliminado de la lista!")
            return
            
    print("No encontramos ese producto para borrar.")

# 6. Función para mostrar todo y cambiar el estado automáticamente
def mostrar_pedidos():
        pedidos = buscar_pedido 
        print("\n---  LISTA DE PEDIDOS ACTUALES ---")
        if len(pedidos) == 0:
            print("La caja está vacía. No hay pedidos.")
        return
pedidos = buscar_pedido
for p in pedidos:
        if p("cantidad") <= 3:
            p( "despacho_rapido") = True
            estado = "⚡ DESPACHO RÁPIDO"
        else:
            p("despacho_rapido") = False
            estado = "PREPARACIÓN NORMAL"

        print(f"{p['producto']} | Cantidad: {p['cantidad']} | Total: ${p['total']} | Estado: {estado}")

programa_encendido = True

while programa_encendido:
    mostrar_menu()
    opcion = input("\nEscoge un número (1 al 6): ")

    if opcion == "1":
        agregar_pedido()
    elif opcion == "2":
        buscar_pedido()
    elif opcion == "3":
        eliminar_pedido()
    elif opcion == "4":
        print("¡Estados actualizados automáticamente!")
        mostrar_pedidos()
    elif opcion == "5":
        mostrar_pedidos()
    elif opcion == "6":
        print("¡Adiós! Gracias por jugar a la cafetería. Ciao ciao.")
        programa_encendido = False # Apagamos todo
    else:
        print("Opción no válida. Presiona un número del 1 al 6, ¡no te distraigas!")