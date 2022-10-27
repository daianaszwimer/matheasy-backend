import numpy as np

from src.interpreters.domain import Response
from src.utils import format_number, search_points

dividing_characters = ["y", ",", "-", "/"]  # TODO: Se puede replicar con la logica del find_near_operator?


def translate_statement(statement, tag):
    # Si es una parabola con vertice y punto
    print("statement")
    if "vertice" in statement:  # TODO: Alguna palabra mas? -> Se puede borrar una vez que este el modelo
        for character in dividing_characters:
            if character in statement:
                result = translate_vertex_point_fun(statement, character)
                return Response(result, tag)
    # Si me dice la funcion que pasa por tales puntos
    # TODO: Si no viene la palabra punto/s? Ej: analiza la funcion que pasa por el origen y por P=(1;2)
    else:
        result = translate_simple_points_fun(statement)
    return Response(result, tag)


# TODO: Ver negativos y comas
# agregar caso del origen en palabras
# Funcion para resolver cuadratica con dato vértice y punto
def translate_vertex_point_fun(statement, word):
    divided_statement = statement.split(word)
    first_part = divided_statement[0]
    second_part = divided_statement[1]
    # Analisis de la primera parte
    if "vertice" in first_part:
        vertex = search_points(first_part)[0]
    if "punto" in first_part or "vertice" not in first_part:
        point = search_points(first_part)[0]
    # Analisis de la segunda parte
    if "vertice" in second_part:
        vertex = search_points(second_part)[0]
    if "punto" in second_part or "vertice" not in second_part:
        point = search_points(second_part)[0]
    # Asigno valores: x, y, xv, yv
    x = format_number(float(point[0]))
    y = format_number(float(point[1]))
    xv = format_number(float(vertex[0]))
    yv = format_number(float(vertex[1]))
    # Calculo a
    a = format_number((y - yv) / ((x - xv) * (x - xv)))
    # Calculo a, b y c
    a1 = format_number(a)  # Coeficiente que multiplica a x^2
    b = format_number(a * xv * -2)  # Coeficiente que multiplica a x
    c = format_number(xv * xv * a + yv)  # Coeficiente independiente
    equation = str(a1) + "*x^2 + " + str(b) + "*x + " + str(c)
    return equation


# Funcion para resolver con dato puntos por los que pasa la funcion
def translate_simple_points_fun(statement):  # TODO ver como escalar esto a cosas mas avanzadas que funcion cuadratica
    quadratic = ["cuadratica", "parabola"]
    # TODO: grado 3? -> Esto estaria bueno agregarlo p/ polinomios en gral y generalizar el armado de la eq
    cubic = ["cubica"]
    is_quadratic = any(word in statement for word in quadratic)
    is_cubic = any(word in statement for word in cubic)
    points = search_points(statement)
    if "origen" in statement:  # TODO: Mejorar
        origin = search_points("(0;0)")[0]
        points.append(origin)
    if not is_quadratic and not is_cubic:
        points = points[:2]

    def x(point):
        if is_quadratic:
            return [float(point[0]) ** 2, float(point[0]), 1]
        if is_cubic:
            return [float(point[0]) ** 3, float(point[0]) ** 2, float(point[0]), 1]
        else:
            return [float(point[0]), 1]

    def y(point):
        return float(point[1])

    xs = list(map(x, points))
    ys = list(map(y, points))
    a = np.array(xs)
    b = np.array(ys)
    resolve = np.linalg.solve(a, b)
    # TODO: Generalizar para polinomios de grado n
    if is_quadratic or is_cubic:
        if is_quadratic:
            first = format_number(round(resolve[0], 2))
            second = format_number(round(resolve[1], 2))
            third = format_number(round(resolve[2], 2))
            equation = str(first) + "*x^2" + " + " + str(second) + "*x + " + str(third)
        else:
            first = format_number(round(resolve[0], 2))  # TODO: Revisar round
            second = format_number(round(resolve[1], 2))
            third = format_number(round(resolve[2], 2))
            fourth = format_number(round(resolve[3], 2))
            equation = str(first) + "*x^3" + " + " + str(second) + "*x^2 + " + str(third) + "*x" + " + " + str(fourth)
    else:
        slope = format_number(round(resolve[0], 2))
        intercept = format_number(round(resolve[1], 2))
        equation = str(slope) + "*x" + " + " + str(intercept)
    return equation
