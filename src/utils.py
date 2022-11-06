import re

import spacy
from recognizers_number import recognize_number, Culture
from src.enums import Exponent
npl = spacy.load('es_core_news_lg')


def search_points(statement):
    r = r"(-?\d+\.?\d*)[;,] *(-?\d+\.?\d*)"
    return re.findall(r, statement)


def format_number(number):
    number = float(number)
    if number.is_integer():
        return int(number)
    else:
        return round(float(number), 6)


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