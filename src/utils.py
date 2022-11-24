import re

import spacy
import unidecode
from recognizers_number import recognize_number, Culture

from src.enums import Exponent

npl = spacy.load('es_core_news_lg')

# TODO: Mover de aca
first_order_operators_dictionary = {"mayor o igual": ">=", "menor o igual": "<=", "igual": "=", "mayor": ">",
                                    "menor": "<"}
first_order_operators_dictionary = {"mayor o igual": ">=", "menor o igual": "<=", "igual": "=", "mayor": ">",
                                    "menor": "<"}
dividing_words = ["y"]
dividing_by_proximity_words = [
    "todo esto ultimo"]  # TODO: El caso "y todo esto ultimo" me va a complicar, revisar como tomarlo
second_order_operators_dictionary = {"mas": "+", "menos": "-", "restado": "-", "resta": "-", "sumado": "+"}
operators_left_dictionary_to_delegate_add_substract = {"sumatoria": "+", "diferencia": "-",
                                                       "suma": "+", "resta": "-"}  # TODO: Revisar
second_second_order_operators_dictionary = {"suma": "+"}  # dividido para no pisar sumatoria
third_order_operators_dictionary = {"multiplicado por": "*", "por": "*", "dividido": "/", "multiplicacion": "*",
                                    "division": "/", "multiplicado": "*", "sobre": "/"}
operators_left_dictionary = {"triple": "3 *", "doble": "2 *", "cuadruple": "4 *", "quintuple": "5 *",
                             "sextuple": "6 *"}  # TODO: Ver caso cuarto, mitad
operators_right_dictionary = {"triplicado": "* 3", "duplicado": "* 2", "cuadruplicado": "* 4", "quintuplicado": "* 5",
                              "sextuplicado": "* 6", "cuadrado": "^2", "cubo": "^3"}  # TODO: Completar
operators_dictionary = {}
operators_dictionary.update(first_order_operators_dictionary)
operators_dictionary.update(second_order_operators_dictionary)
operators_dictionary.update(operators_left_dictionary_to_delegate_add_substract)
operators_dictionary.update(second_second_order_operators_dictionary)
operators_dictionary.update(third_order_operators_dictionary)
operators_dictionary.update(operators_left_dictionary)
operators_dictionary.update(operators_right_dictionary)

math_terms = ["funcion", "dominio", "imagen", "pendiente", "vertice", "ordenada", "al", "origen", "ord", "punto",
              "puntos", "todo", "esto", "ultimo"]

from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def fix_near_operators(statement):
    operators = list(operators_dictionary.keys()) + math_terms
    final_statement = statement
    statement = npl(statement)
    for token in statement:
        final_matches = [(k, similar(k, token.text)) for k in operators if similar(k, token.text) >= 0.8]
        final_matches.sort(key=lambda a: a[1], reverse=True)
        if len(final_matches) >= 1:
            final_statement = final_statement.replace(token.text, final_matches[0][0])
    return final_statement


def is_valid_statement(statement):
    statement = statement.lower()
    statement = unidecode.unidecode(statement)
    statement = npl(statement)

    has_any_num = False
    has_any_operator = False

    for token in statement:
        if token.pos_ == "NUM":
            has_any_num = True
        if token.text.isnumeric():
            has_any_num = True
    if has_numbers(statement.text):
        has_any_num = True

    for operator in operators_dictionary.keys():
        if operator in statement.text:
            has_any_operator = True
    for operator in operators_dictionary.values():
        if operator in statement.text:
            has_any_operator = True
    for operator in math_terms:
        if operator in statement.text:
            has_any_operator = True
    return has_any_num and has_any_operator


def has_numbers(statement):
    return bool(re.search(r'\d', statement))


def search_points(statement):
    r = r"(-?\d+\.?\d*)[;,] *(-?\d+\.?\d*)"
    return re.findall(r, statement)


# Check that string doesn't have any letters, only numbers and . or ,
def string_is_numeric(token):  # TODO: Se puede unificar con is_negative_or_float_number ?
    r1 = r"\d*\,?\d*"
    r2 = r"\d*\.?\d*"
    letters = r"[a-zA-Z]"
    return (re.match(r1, token) or re.match(r2, token)) and re.search(letters, token) is None


def format_number(number):
    number = float(number)
    if number.is_integer():
        return int(number)
    else:
        return round(float(number), 3)


def search_number(statement):
    statement = npl(statement)
    for token in statement:
        if token.pos_ == "NUM" or token.text.isnumeric() or is_negative_or_float_number(token.text):
            if token.text.isnumeric():
                return token.text
            else:  # Es un numero en palabras
                number = recognize_number(token.text, Culture.Spanish)[0].resolution["value"]
                return number


def is_negative_or_float_number(number):
    r = r'-?\d+[,.]?\d*'
    is_float = re.match(number, r)
    return (number[0] == '-' and len(number) > 1 and number[1:].isnumeric()) or is_float


def get_root_of_equation(equation):
    if "<=" in equation:
        return "<="
    if ">=" in equation:
        return ">="
    if "<" in equation:
        return "<"
    if ">" in equation:
        return ">"
    else:
        return "="


def get_exponent_of_equation(equation):
    if "^2" in equation:
        return Exponent.TWO
    if "^3" in equation:
        return Exponent.THREE
    else:
        return Exponent.ONE
