def sum(a, b):
    """
    >>> sum(1, 2)
    3
    
    >>> sum(5, 7)
    12
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: No se puede dividir por cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b