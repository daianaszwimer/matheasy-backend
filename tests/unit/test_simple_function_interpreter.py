import src.interpreters.simpleFunctionInterpreter as interpreter


def test_1():
    response = interpreter.translate_statement("f(x) = (x - 3)/(x + 2)", "funcion-explicita")
    assert response.expression == "(x-3)/(x+2)"


def test_2():
    response = interpreter.translate_statement("y = (x - 3)/(x + 2)", "funcion-explicita")
    assert response.expression == "(x-3)/(x+2)"


def test_3():
    response = interpreter.translate_statement("f(x) = 7x+6", "funcion-explicita")
    assert response.expression == "7x+6"


def test_4():
    response = interpreter.translate_statement("y = x ^ 2 + x + 9", "funcion-explicita")
    assert response.expression == "x^2+x+9"


def test_5():
    response = interpreter.translate_statement("y = x+8", "funcion-explicita")
    assert response.expression == "x+8"


def test_6():
    response = interpreter.translate_statement(
        "Analiza la funcion f(x) = -(2x + 9/2)/(x + 1), obtene dominio imagen y saraza", "funcion-explicita")
    assert response.expression == "-(2x+9/2)/(x+1)"


def test_7():
    response = interpreter.translate_statement("Realiza el analisis de la funcion (x - 3)/(x + 2)", "funcion-explicita")
    assert response.expression == "(x-3)/(x+2)"


def test_8():
    response = interpreter.translate_statement("Analiza la funcion x+2, calcula todas las cositas",
                                               "funcion-explicita")
    assert response.expression == "x+2"


def test_9():
    response = interpreter.translate_statement(
        "Analiza la parabola y = x ^ 2 + 3x - 18, saca vertice y ordenada al origen", "funcion-explicita")
    assert response.expression == "x^2+3x-18"


def test_10():
    response = interpreter.translate_statement("Analiza y = x-16+8, indica dominio e imagen", "funcion-explicita")
    assert response.expression == "x-16+8"
