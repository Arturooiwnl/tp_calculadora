# Arturo Benicio Perotto - 113 

def sumar(a:int, b:int)->int:
    """Suma

    Args:
        a (int): Sumando
        b (int): Sumando

    Returns:
        int: Total
    """
    resultado = a + b
    return resultado

def restar(a:int, b:int)->int:
    """Resta 

    Args:
        a (int): Minuendo
        b (int): Sustraendo

    Returns:
        int: Diferencia
    """
    resultado = a - b
    return resultado

def dividir(a:int, b:int)->int:
    """Division

    Args:
        a (int): Dividendo
        b (int): Divisor

    Returns:
        int: Cociente
    """
    if b == 0:
        print("ERROR | No se puede dividir por 0.")
    try:
        resultado = a/b
        return resultado
    except ZeroDivisionError:
        print("ERROR | Error inesperado al realizar la división.")



def multiplicar(a:int, b:int)->int:
    """Multiplicacion 

    Args:
        a (int): Multiplicando
        b (int): Multiplicador

    Returns:
        int: Producto
    """
    resultado = a * b
    return resultado

def factorial(n:int)->int:
    """Factorial

    Args:
        n (int): Numero que se quiere factorizar

    Returns:
        int: Resultado
    """
    if n < 0:
        print("ERROR | El valor debe ser un entero positivo.")
    elif n == 0:
        return 1
    else:
        fac= 1
        for i in range(2, n +1):
            fac*=i
        resultado = fac
        return resultado

#####################################################

print(factorial(-1))

