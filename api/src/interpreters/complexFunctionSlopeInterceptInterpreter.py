from src.interpreters.domain import Response
from src.utils import search_number, npl, search_points, format_number

dividing_characters = ["y", ",", "-", "/"]  # TODO: Se puede replicar con la logica del find_near_operator?
intercepts = ["ordenada", "ord.", "ordenada al origen", "ord. al origen", "ord al origen",
              "ordenada en el origen", "ord en el origen", "ord. en el origen", "punto"]
slopes = ["pendiente"]


def translate_statement(statement, tag):
    if any(word in statement for word in intercepts + slopes):
        for character in dividing_characters:
            if character in statement:
                result = translate_intercept_and_slope_fun(statement, character)
                return Response(result, tag)


# TODO: Revisar numeros con coma
# Funcion para resolver funciones lineales cuando nos dan el dato de la ordenada al origen y la pendiente o un punto
def translate_intercept_and_slope_fun(statement, character):
    divided_statement = statement.split(character)
    first_part = npl(divided_statement[0])
    second_part = npl(divided_statement[1])
    # Busqueda pendiente
    for token in first_part:
        if token.text in slopes:
            slope = search_number(first_part)
    for token in second_part:
        if token.text in slopes:
            slope = search_number(second_part)
    # Busqueda ordenada al origen
    for token in first_part:
        if token.text in intercepts:
            intercept = search_intercept(token, first_part, slope)
    for token in second_part:
        if token.text in intercepts:
            intercept = search_intercept(token, second_part, slope)
    equation = str(slope) + "*x" + " + " + str(intercept)
    return equation


def search_intercept(token, part, slope):
    if token.text != "punto":
        return search_number(part)
    else:
        point = search_points(part.text)[0]
        x = format_number(float(point[0]))
        y = format_number(float(point[1]))
        intercept = y - format_number(slope) * x
        return intercept
