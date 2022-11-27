import src.interpreters.simpleEquationInterpreter as interpreter


def test_1():
    response = interpreter.translate_statement(
        "x+2=9", "ecuacion-explicita")
    assert response.expression == "x+2=9"


def test_2():
    response = interpreter.translate_statement(
        "2+x=9", "ecuacion-explicita")
    assert response.expression == "2+x=9"


def test_3():
    response = interpreter.translate_statement(
        "x + 2 = 9", "ecuacion-explicita")
    assert response.expression == "x + 2 = 9"


def test_4():
    response = interpreter.translate_statement(
        "(x + 2 =9)", "ecuacion-explicita")
    assert response.expression == "(x + 2 =9)"


def test_5():
    response = interpreter.translate_statement(
        "(x + 2) = 9", "ecuacion-explicita")
    assert response.expression == "(x + 2) = 9"


def test_6():
    response = interpreter.translate_statement(
        "Resolve la ecuacion: (x + 2) = 9", "ecuacion-explicita")
    assert response.expression == "(x + 2) = 9"


def test_7():
    response = interpreter.translate_statement(
        "Despeja x de la siguiente ecuacion (x + 2) = 9", "ecuacion-explicita")
    assert response.expression == "(x + 2) = 9"


def test_8():
    response = interpreter.translate_statement(
        "Resolve x de la ecuacion x + 2 = 9", "ecuacion-explicita")
    assert response.expression == "x + 2 = 9"


def test_9():
    response = interpreter.translate_statement(
        "Resolve x de la ecuacion x + 2 = 9 cosas adicionales as da sd", "ecuacion-explicita")
    assert response.expression == "x + 2 = 9"


def test_10():
    response = interpreter.translate_statement(
        "Resolve x la ecuacion -2 + x + 2 = 9 cosas adicionales", "ecuacion-explicita")
    assert response.expression == "-2 + x + 2 = 9"


def test_11():
    response = interpreter.translate_statement(
        "-2 + x + 2 = 9", "ecuacion-explicita")
    assert response.expression == "-2 + x + 2 = 9"


def test_12():
    response = interpreter.translate_statement(
        "-2 + x + 2 >= 9", "ecuacion-explicita")
    assert response.expression == "-2 + x + 2 >= 9"


def test_13():
    response = interpreter.translate_statement(
        "-x + 4 + 2 >= 9", "ecuacion-explicita")
    assert response.expression == "-x + 4 + 2 >= 9"


def test_14():
    response = interpreter.translate_statement(
        "Resolve x la ecuacion: -x + 4 + 2 >= 9", "ecuacion-explicita")
    assert response.expression == "-x + 4 + 2 >= 9"


def test_15():
    response = interpreter.translate_statement(
        "Resolve x la ecuacion: -x + 4 + 2 >= 9 adicional", "ecuacion-explicita")
    assert response.expression == "-x + 4 + 2 >= 9"


def test_16():
    response = interpreter.translate_statement(
        "-5x + 4 + 2 >= 9", "ecuacion-explicita")
    assert response.expression == "-5x + 4 + 2 >= 9"


def test_17():
    response = interpreter.translate_statement(
        "Resolve x+2", "ecuacion-explicita")
    assert response.expression == "x+2"


def test_18():
    response = interpreter.translate_statement(
        "x+2", "ecuacion-explicita")
    assert response.expression == "x+2"


def test_19():
    response = interpreter.translate_statement(
        "x", "ecuacion-explicita")
    assert response.expression == "x"


def test_20():
    response = interpreter.translate_statement(
        "Despejá la x en 5x + 2 = 10", "ecuacion-explicita")
    assert response.expression == "5x + 2 = 10"
