from src.utils import is_valid_statement


def test_1():
    statement = "Cual es el numero que sumado 8 todo esto ultimo multiplicado 16 es menor a cien?"
    assert is_valid_statement(statement) == True


def test_2():  # FIXME: Poner duplicado en vez de por 2
    statement = "Despejar el valor de x que satisface que: 5 dividido 2 mas x, todo esto ultimo por 2 es mayor o igual a 10"
    assert is_valid_statement(statement) == True


def test_3():
    statement = "Resolve la x que sumado a 5 y multiplicado por 9 es igual a 11"
    assert is_valid_statement(statement) == True


def test_4():
    statement = "Resolve la x que sumado a 5 al cuadrado es menor o igual al doble de 11"
    assert is_valid_statement(statement) == True


def test_5():
    statement = "Analiza la funcion que tiene pendiente 4 y pasa por el punto (3;5)"
    assert is_valid_statement(statement) == True


def test_6():
    statement = "Realiza el analisis de la funcion lineal que tiene como pendiente 3 y como ordenada al origen 6"
    assert is_valid_statement(statement) == True


def test_7():
    statement = "Hola como va probando probando !! ?? 1 2 3 4 "
    assert is_valid_statement(statement) == False
