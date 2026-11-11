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
print("7 elegir operación")

eleccion = int(input())

if eleccion == 1:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero + segundo_numero)
    print(resultado)
    
elif eleccion == 2:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero - segundo_numero)
    print(resultado)

elif eleccion == 3:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero * segundo_numero)
    print(resultado)
    
elif eleccion == 4:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero / segundo_numero)
    print(resultado)

elif eleccion == 5:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())

    resultado = str(primer_numero % segundo_numero)
    print(resultado)

elif eleccion == 6:
    print("Digite un numero")
    primer_numero = int(input())
    print("Digite el segundo numero")
    segundo_numero = int(input())
    print("Digite el tercer numero")
    tercer_numero = int(input())

    resultado = str(primer_numero + segundo_numero + tercer_numero)
    print(resultado)
    
elif eleccion == 7:
    print("Digite un numero")
    primer_numero = str(input())
    print("Digite el segundo numero")
    segundo_numero = str(input())
    print("elige la operación")
    operacion = str(input())

    resultado = str(eval(primer_numero + operacion + segundo_numero))
    print(resultado)