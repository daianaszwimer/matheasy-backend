import pytest
import src.modelPredictor as modelPredictor
from src.modelTrainer import model, X_train, y_train

@pytest.fixture
def modelo():
    model.fit(X_train, y_train)
    return model
    

def test_despeja_la_x_de_ecuacion_es_ecuacion_explicita(modelo):
    prediccion = modelPredictor.predict("Despeja la x de la siguiente ecuacion x+2=4")
    assert prediccion == "ecuacion-explicita"

def test_despeja_la_x_de_inecuacion_es_ecuacion_explicita(modelo):
    prediccion = modelPredictor.predict("despejar x de la siguiente ecuacion: x + 8 < 9")
    assert prediccion == "ecuacion-explicita"

def test_resolve_inecuacion_mayor_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("Resolvé la ecuación x más 63 dividido 63 es mayor a 55.")
    assert prediccion == "ecuacion-implicita"

def test_cual_es_el_numero_que_cumple_condicion_es_mayor_a_otro_numero_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("cual es el numero que multiplicado 2 y sumado 7 es mayor a 100?")
    assert prediccion == "ecuacion-implicita"

def test_cual_es_el_numero_que_cumple_condicion_es_mayor_a_otro_numero_letras__es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("cual es el numero que multiplicado dos y sumado cuatro es mayor a ochenta?")
    assert prediccion == "ecuacion-implicita"

def test_analiza_la_funcion_es_funcion_explicita(modelo):
    prediccion = modelPredictor.predict("Analiza la funcion y = 2*x + 8")
    assert prediccion == "funcion-explicita"

def test_analiza_la_funcion_que_pasa_por_puntos_es_funcion_implicita_puntos(modelo):
    prediccion = modelPredictor.predict("Analiza la funcion que pasa por los puntos (1;2) y (2;1)")
    assert prediccion == "funcion-implicita-puntos"

def test_analiza_la_parabola_que_pasa_por_tres_puntos_es_funcion_implicita_puntos(modelo):
    prediccion = modelPredictor.predict("Analiza la parabola que pasa por los puntos (1;2), (2;4) y (3;2)")
    assert prediccion == "funcion-implicita-puntos"

def test_analiza_la_parabola_que_pasa_por_vertice_es_funcion_implicita_vertice(modelo):
    prediccion = modelPredictor.predict("Analiza la parabola que tiene su vertice en (1,2) y pasa por el punto (2,4)")
    assert prediccion == "funcion-implicita-vertice"

def test_funcion_que_tiene_pendiente_y_ordenada_es_funcion_implicita_po(modelo):
    prediccion = modelPredictor.predict("Analiza función que tiene ordenada -5 y pendiente 6")
    assert prediccion == "funcion-implicita-po"


