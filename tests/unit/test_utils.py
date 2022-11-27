from src.utils import is_valid_statement, fix_near_operators


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


def test_8():
    statement = "Obtener el análisis de la siguiente funcion : F(x) =-5x +2"
    assert is_valid_statement(statement) == True


# Tests fix enunciado mal escrito
def test_9():
    statement = "cual es el numero que multiplicaod 2 y sumdo 5 es igual a 10?"
    assert fix_near_operators(statement) == "cual es el numero que multiplicado 2 y sumado 5 es igual a 10?"


def test_10():
    statement = "resolve la sumatrioa de 5, 6 y 9 tod esto ultmio dividid 10"
    assert fix_near_operators(statement) == "resolve la sumatoria de 5, 6 y 9 todo esto ultimo dividido 10"


def test_11():
    statement = "analiza la funcin que pasa por el punot P=(1;2) y por Q=(2;3)"
    assert fix_near_operators(statement) == "analiza la funcion que pasa por el punto P=(1;2) y por Q=(2;3)"


def test_12():
    statement = "analiza la fincion que pasa por el pnuto P=(1;2) y tiene su vortice en (0;0)"
    assert fix_near_operators(
        statement) == "analiza la funcion que pasa por el punto P=(1;2) y tiene su vertice en (0;0)"


def test_13():
    statement = "realiza el analisis de la fyncion que tiene pendinte 1 y ordnada al orgien 6"
    assert fix_near_operators(
        statement) == "realiza el analisis de la funcion que tiene pendiente 1 y ordenada al origen 6"


def test_14():
    statement = "cual es el numero que restad 10 y mutliplicado pr 4 es menr o igul a 100?"
    assert fix_near_operators(
        statement) == "cual es el numero que restado 10 y multiplicado por 4 es menor o igual a 100?"
