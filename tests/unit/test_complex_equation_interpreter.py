import src.interpreters.complexEquationInterpreter as interpreter


# Se prueba sumado, to do esto ultimo, menor, numero en palabras
def test_1():
    response = interpreter.translate_statement(
        "Cual es el numero que sumado 8 todo esto ultimo multiplicado 16 es menor a cien?", "ecuacion-implicita")
    assert response.expression == "((x + 8) * 16) < 100"


# Se prueba dividido, mas, por, mayor o igual
def test_2():  # FIXME: Poner duplicado en vez de por 2
    response = interpreter.translate_statement(
        "Despejar el valor de x que satisface que: 5 dividido 2 mas x, todo esto ultimo por 2 es mayor o igual a 10",
        "ecuacion-implicita")
    assert response.expression == "(((5 / 2) + x) * 2) >= 10"


# Se prueba palabra divisoria seguido de un operador compuesto como multiplicado por
def test_3():
    response = interpreter.translate_statement(
        "Resolve la x que sumado a 5 y multiplicado por 9 es igual a 11",
        "ecuacion-implicita")
    assert response.expression == "((x + 5) * 9) = 11"


# Se prueba ecuacion con operadores de derecha e izquierda
def test_4():
    response = interpreter.translate_statement(
        "Resolve la x que sumado a 5 al cuadrado es menor o igual al doble de 11",
        "ecuacion-implicita")
    assert response.expression == "(x + (5 ^2)) <= (2 * 11)"
