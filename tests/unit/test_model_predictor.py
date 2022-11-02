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

#FIXME
def test_resolve_la_x_de_ecuacion_es_ecuacion_explicita(modelo):
    prediccion = modelPredictor.predict("Resolvé la x de x+(2+16) +4 = 5")
    assert prediccion == "ecuacion-explicita"

def test_indica_conjunto_solucion_de_la_x_de_ecuacion_es_ecuacion_explicita(modelo):
    prediccion = modelPredictor.predict("Indicá el conjunto solución de la x de x+(2+16) +4 = 5")
    assert prediccion == "ecuacion-explicita"

#FIXME
def test_resolve_la_x_de_ecuacion_compleja_es_ecuacion_explicita(modelo):
    prediccion = modelPredictor.predict("Resolve la x de x*(2+16) +4 = 5")
    assert prediccion == "ecuacion-explicita"

def test_resolve_inecuacion_mayor_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("Resolvé la ecuación x más 63 dividido 63 es mayor a 55.")
    assert prediccion == "ecuacion-implicita"

def test_cual_es_el_numero_que_cumple_condicion_es_mayor_a_otro_numero_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("cual es el numero que multiplicado 2 y sumado 7 es mayor a 100?")
    assert prediccion == "ecuacion-implicita"

def test_cual_es_el_numero_que_cumple_condicion_es_mayor_a_otro_numero_letras_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("cual es el numero que multiplicado dos y sumado cuatro es mayor a ochenta?")
    assert prediccion == "ecuacion-implicita"

def test_cual_es_el_numero_que_sumado_8_es_menor_a_cien_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("Cual es el numero que sumado 8 es menor a cien? ")
    assert prediccion == "ecuacion-implicita"

def test_que_numero_elevado_al_cuadrado_y_sumado_5_es_igual_a_148_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("Que numero elevado al cuadrado y sumado 5 es igual a 148?")
    assert prediccion == "ecuacion-implicita"  

def test_analiza_la_funcion_es_funcion_explicita(modelo):
    prediccion = modelPredictor.predict("Analiza la funcion y = 2*x + 8")
    assert prediccion == "funcion-explicita"

def test_analiza_la_funcion_que_pasa_por_puntos_es_funcion_implicita_puntos(modelo):
    prediccion = modelPredictor.predict("Analiza la funcion que pasa por los puntos (1;2) y (2;1)")
    assert prediccion == "funcion-implicita-puntos"

def test_indica_dominio_imagen_de_la_funcion_que_pasa_por_puntos_es_funcion_implicita_puntos(modelo):
    prediccion = modelPredictor.predict("Indicá dominio e imagen de la funcion que pasa por los puntos (1;2) y (2;1)")
    assert prediccion == "funcion-implicita-puntos"

def test_analiza_la_parabola_que_pasa_por_tres_puntos_es_funcion_implicita_puntos(modelo):
    prediccion = modelPredictor.predict("Analiza la parabola que pasa por los puntos (1;2), (2;4) y (3;2)")
    assert prediccion == "funcion-implicita-puntos"

def test_analiza_la_parabola_que_pasa_por_vertice_es_funcion_implicita_vertice(modelo):
    prediccion = modelPredictor.predict("Analiza la parabola que tiene su vertice en (1,2) y pasa por el punto (2,4)")
    assert prediccion == "funcion-implicita-vertice"

def test_funcion_que_tiene_pendiente_y_ordenada_es_funcion_implicita_po(modelo):
    prediccion = modelPredictor.predict("Analiza la función que tiene ordenada -5 y pendiente 6")
    assert prediccion == "funcion-implicita-po"

def test_indica_dominio_imagen_de_funcion_que_tiene_pendiente_y_ordenada_es_funcion_implicita_po(modelo):
    prediccion = modelPredictor.predict("Indicá el dominio e imagen de la función que tiene ordenada -5 y pendiente 6")
    assert prediccion == "funcion-implicita-po"

def test_oracion_coloquial_es_funcion_implicita(modelo):
    prediccion = modelPredictor.predict("Cuál es la función de x sumado a 10 y multiplicado por 5 es igual a 7?")
    assert prediccion == "funcion-implicita"    

def test_determina_oracion_coloquial_es_funcion_implicita(modelo):
    prediccion = modelPredictor.predict("Determiná la función de x sumado a 10 y multiplicado por 5 es igual a 7?")
    assert prediccion == "funcion-implicita"    

def test_funcion_que_pasa_por_vertice_es_funcion_implicita_vertice(modelo):
    prediccion = modelPredictor.predict("Qué función tiene su vértice en el punto (2,2) y pasa por (10,6)?")
    assert prediccion == "funcion-implicita-vertice"  

def test_cual_es_la_diferencia_entre_8_y_5_es_ecuacion_implicita(modelo):
    prediccion = modelPredictor.predict("Cual es la diferencia de 8 y 5?")
    assert prediccion == "ecuacion-implicita"  

#FIXME
def test_f_es_igual_a_una_expresion_es_funcion_explicita(modelo):
    prediccion = modelPredictor.predict("f(x) = (x - 3)/(x + 2)")
    assert prediccion == "funcion-explicita"

#FIXME
def test_y_es_igual_a_una_expresion_es_funcion_explicita(modelo):
    prediccion = modelPredictor.predict("y = (x - 3)/(x + 2)")
    assert prediccion == "funcion-explicita"

def test_halla_conjuntos_de_funcion_cuadratica_dado_vertice_y_punto(modelo):
    prediccion = modelPredictor.predict("Halla función cuadrática tal que vértice = (3; -2) y pase por P = (1; 2). Graficala, halla Co, f(0), C+ y C-.")
    assert prediccion == "funcion-implicita-vertice"

def test_halla_conjuntos_de_funcion_lineal_dado_puntos(modelo):
    prediccion = modelPredictor.predict("Halla la función lineal que pasa por P = (3; -2) y Q = (2; -1). Graficala, halla ceros, o. al origen. Indica C+ y C-.")
    assert prediccion == "funcion-implicita-puntos"