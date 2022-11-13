import src.interpreters.complexFunctionSlopeInterceptInterpreter as interpreter


# Se prueba funcion a partir de pendiente y punto por el que pasa
def test_1():
    response = interpreter.translate_statement(
        "Analiza la funcion que tiene pendiente 4 y pasa por el punto (3;5)", "function")
    assert response.expression == "4*x + -7"


# Se prueba funcion a partir de pendiente y ordenada al origen
def test_2():
    response = interpreter.translate_statement(
        "Realiza el analisis de la funcion lineal que tiene como pendiente 3 y como ordenada al origen 6", "function")
    assert response.expression == "3*x + 6"
