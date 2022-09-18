from src.interpreters.domain import Response
from src.utils import search_number, npl

dividing_characters = ["y", ",", "-", "/"]  # TODO: Se puede replicar con la logica del find_near_operator?
intercepts = ["ordenada", "ord.", "ordenada al origen", "ord. al origen", "ord al origen",
              "ordenada en el origen", "ord en el origen", "ord. en el origen"]
slopes = ["pendiente"]


def translate_statement(statement, tag):
    if any(word in statement for word in intercepts + slopes):
        for character in dividing_characters:
            if character in statement:
                result = translate_intercept_and_slope_fun(statement, character)
                return Response(result, tag)


# TODO: Revisar numeros con coma
# Funcion para resolver funciones lineales cuando nos dan el dato de la ordenada al origen y la pendiente
def translate_intercept_and_slope_fun(statement, character):
    divided_statement = statement.split(character)
    first_part = npl(divided_statement[0])
    second_part = npl(divided_statement[1])
    # Analisis de la primera parte
    for token in first_part:
        if token.text in intercepts:
            intercept = search_number(first_part)
    for token in first_part:
        if token.text in slopes:
            slope = search_number(first_part)
    # Analisis de la segunda parte
    for token in second_part:
        if token.text in intercepts:
            intercept = search_number(second_part)
    for token in second_part:
        if token.text in slopes:
            slope = search_number(second_part)
    equation = str(slope) + "*x" + " + " + str(intercept)
    return equation
