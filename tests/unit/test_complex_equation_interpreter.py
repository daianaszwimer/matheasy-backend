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
