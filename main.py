'''
print("Digite un numero")
primer_numero = int(input())
print("Digite el segundo numero")
segundo_numero = int(input())

resultado = str(primer_numero + segundo_numero)


print("El resultado de la suma es: " + resultado)
'''

print("¿Que operación deseas realizar?")
print("1 Sumar")
print("2 Restar")
print("3 Multiplicar")
print("4 Dividir")
print("5 Modulo")
print("6 Sumar tres números")

eleccion = int(input())

if eleccion == 1:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero + segundo_numero)
    
elif eleccion == 2:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero - segundo_numero)

elif eleccion == 3:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero * segundo_numero)
elif eleccion == 4:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero / segundo_numero)

elif eleccion == 5:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero % segundo_numero)

elif eleccion == 6:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())
    print("Digite el tercer numero")
    tercer_numero = int(input())

    resultado = str(primer_numero + segundo_numero + tercer_numero)