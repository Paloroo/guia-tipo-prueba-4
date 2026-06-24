def mostrar_menu():
    
    print("------------------Menu Principal-------------------")
    print("1. Agregar ticket")
    print("2. Buscar ticket")
    print("3. Eliminar ticket")
    print("4. Actualizar estado")
    print("5. Mostrar tickets")
    print("6. Salir")
    print("--------------------------------------------------")
mostrar_menu()

def leer_opcion():
    opcion = 0 

    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Seleccione una opcion (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Error la opcion debe estar entre 1 y 6.")
        except ValueError: 
            print("Error: Debe ser numero entero.")

    return opcion      
leer_opcion()

def  validar_actividad(valor):
    return valor.strip() != ""


def validar_ponderacion(valor):
    return 1 <= valor <= 100

def validar_nota(valor):
    return valor > 0

def agregar_evaluación(evaluaciones):
    actividad = input("Nombre de la actividad: ")

    try:
        ponderacion = int(input("Ponderacion de la actividad: "))
        nota = float(input("Nota obtenida: "))
    except ValueError:
        print("Error los datos numericos no tienen el formato esperado.")
        return
    
    if not validar_actividad(actividad):
        print("Error: No puede estar vacio ni ser solo espacios.")
    elif not validar_ponderacion(ponderacion):
        print("Error: Debe ser un numero entero entre 1 y 100.")
    elif not validar_nota(nota):
        print("Error: Debe ser un numero decimal mayor que cero.")
    else:
        nueva_evaluacion = {
            "actividad": actividad.strip(),
            "ponderacion": ponderacion,
            "nota": nota,
            "aprobada": False
        }    
        evaluaciones.append(nueva_evaluacion)
        print("Evaluacion agregada correctamente")
         
def buscar_evaluación(evaluaciones, dato_busqueda):
    posicion = -1
    i = 0

    while i < len(evaluaciones) and posicion == -1:
        if evaluaciones[i]["actividad"] == dato_busqueda:
            posicion = i
        i += 1

    return posicion

def eliminar_evaluación(evaluaciones):
    dato_busqueda = input("Ingrese el valor de nombre de la actividad a eliminar: ").strip()
    posicion = buscar_evaluación(evaluaciones, dato_busqueda)

    if posicion != -1:
        evaluaciones.pop(posicion)
        print("Evaluación eliminado correctamente.")
    else:
        print(f"El registro '{dato_busqueda}' no se encuentra registrado.")

def actualizar_estado(evaluaciones):
    for evaluación in evaluaciones:
        if evaluación["nota"] >= 4.0:
            evaluación["aprobada"] = True
    else:
        evaluación["aprobada"] = False

def mostrar_evaluaciones(evaluaciones):
    actualizar_estado(evaluaciones)
    print("=== LISTA DE EVALUACIONES ===")

    if len(evaluaciones) == 0:
        print("No hay registros para mostrar.")
    else:
        for evaluación in evaluaciones:
            print(f"Nombre de la actividad: {evaluación['actividad']}")
            print(f"Ponderación de la actividad: {evaluación['ponderacion']}")
            print(f"Nota obtenida: {evaluación['nota']}")
    if evaluación["aprobada"]:
        print("Estado: APROBADA")
    else:
        print("Estado: REQUIERE MEJORA")
    print("********************************************")

evaluaciones = []
continuar = True
while continuar:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_evaluación(evaluaciones)
    elif opcion == 2:
        dato_busqueda = input("Ingrese el valor de nombre de la actividad a buscar: ").strip()
        posicion = buscar_evaluación(evaluaciones, dato_busqueda)
        if posicion != -1:
            print("Registro encontrado:")
            print(evaluaciones[posicion])   
        else:
            print("No se encontró el registro solicitado.")
    elif opcion == 3:
        eliminar_evaluación(evaluaciones)
    elif opcion == 4:
        actualizar_estado(evaluaciones)
        print("Estados actualizados correctamente.")
    elif opcion == 5:
        mostrar_evaluaciones(evaluaciones)
    else:
        continuar = False
        
print("Gracias por usar el sistema de evaluaciones. Hasta la próxima.")
