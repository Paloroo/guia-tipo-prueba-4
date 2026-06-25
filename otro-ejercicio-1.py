def calcular_promedio(nota1,nota2,nota3):
    promedio = (nota1+nota2+nota3)/3
    return promedio

print("====promedio de notas====") 
notas1 = float(input("Ingrese su primera nota: "))  
notas2 = float(input("Ingrese su segunda nota: "))
notas3 = float(input("Ingrese su tercera nota: "))

final = calcular_promedio(notas1,notas2,notas3)
final = round(final,2)

if final >= 4.0:
    print("Estado: Aprobado")
else:
    print("Estado: reprobado")    