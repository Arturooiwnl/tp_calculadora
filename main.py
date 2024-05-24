# Arturo Benicio Perotto - 113 
# TP calculadora - main

from operaciones import *
from os import system

flag_primer_valor = False
flag_segundo_valor = False

def pause():
    system("pause")

def clean_screen():
    system("cls")

def pedir_num_a():
    a = None
    while a is None or a < 0:
        try:
            a = int(input("\nCALCULADORA | Ingresar el primer valor: "))
            if a >= 0:
                print(f"CALCULADORA | El primer valor es: x = {a}.")
            else:
                print("ERROR | El valor debe ser mayor o igual a 0.")
        except ValueError:
            print("ERROR | Ingresa de nuevo el valor.")
    return a

def pedir_num_b():
    b = None
    while b is None or b < 0:
        try:
            b = int(input("\nCALCULADORA | Ingresar el segundo valor: "))
            if b >= 0:
                print(f"CALCULADORA | El segundo valor es: y = {b}.")
            else:
                print("ERROR | El valor debe ser mayor o igual a 0.")
        except ValueError:
            print("ERROR | Ingresa de nuevo el valor.")
    return b

def operaciones_menu():
    print("           Operaciones")
    print("[1]- Suma (+)")
    print("[2]- Resta (-)")
    print("[3]- Multiplicación (*)")
    print("[4]- División (/)")
    print("[5]- Factorización (!)")
    print("[6]- Realizar todas las operaciones")
    return input("Seleccione una opción: ")

def options_menu():
    clean_screen()
    print("  Menú de opciones")
    print("")
    print("[1]- Ingresar el primer valor ")
    print("[2]- Ingresar el segundo valor ")
    print("[3]- Seleccione un operador ")
    print("[4]- Salir ")
    return input("Seleccione una opción: ")

def realizar_all_operaciones(a, b):
    print(f"Suma: {sumar(a, b)}")
    print(f"Resta: {restar(a, b)}")
    print(f"División: {dividir(a, b)}")
    print(f"Multiplicación: {multiplicar(a, b)}")
    print(f"Factorial de {a}: {factorial(a)}")
    print(f"Factorial de {b}: {factorial(b)}")

def realizar_operaciones(a, b):
    while True:
        operacion = operaciones_menu()
        match operacion:
            case "1":
                print(f"Suma: {sumar(a, b)}")
            case "2":
                print(f"Resta: {restar(a, b)}")
            case "3":
                print(f"Multiplicación: {multiplicar(a, b)}")
            case "4":
                print(f"División: {dividir(a, b)}")
            case "5":
                print(f"Factorial de {a}: {factorial(a)}")
                print(f"Factorial de {b}: {factorial(b)}")
            case "6":
                realizar_all_operaciones(a, b)
            case _:
                print("ERROR | Selección no válida.")
                continue
        break

while True:
    opcion = options_menu()
    if opcion == "1":
        primer_valor = pedir_num_a()
        flag_primer_valor = True
    elif opcion == "2":
        if flag_primer_valor:
            segundo_valor = pedir_num_b()
            flag_segundo_valor = True
        else:
            print("ERROR | Debes ingresar el primer valor primero.")
    elif opcion == "3":
        if flag_segundo_valor:
            realizar_operaciones(primer_valor, segundo_valor)
        else:
            print("ERROR | Debes ingresar el segundo valor.")
    elif opcion == "4":
        print("CALCULADORA | Saliendo de la calculadora...")
        flag_primer_valor = False
        flag_segundo_valor = False
        break
    pause()
