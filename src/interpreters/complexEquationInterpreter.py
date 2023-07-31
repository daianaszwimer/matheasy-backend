import re

import spacy
from recognizers_number import recognize_number, Culture

import src.interpreters.addSubstractInterpreter as addSubstractInterpreter
from src.interpreters.domain import Response
from src.utils import string_is_numeric

npl = spacy.load('es_core_news_lg')
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


def find_near_operator(dividing_word, sentence):
    for operator in operators_dictionary.keys():
        operator_occurence_index = sentence.find(operator)
        if operator_occurence_index != -1:
            r = r"-?\d+\.?\d*"
            # TODO si hay un numero en palabras no se va a encontrar aca
            if re.search(r, sentence).start() < operator_occurence_index:
                return None
            else:
                return dividing_word + sentence[:operator_occurence_index + len(operator)]


def search_math_term(sentence):
    statement = npl(sentence)
    for operator in first_order_operators_dictionary.keys():
        if operator in statement.text:
            return "operator", operator, "first_order"
    for word in dividing_words:
        if word in statement.text:
            start_index_word = statement.text.rfind(word)
            end_index_word = start_index_word + len(word)
            right_sentence = statement.text[end_index_word:-1]
            near_operator = find_near_operator(word, right_sentence)
            if near_operator is not None:
                return "operator", near_operator, "divisory"
    for word in dividing_by_proximity_words:
        if word in statement.text:
            start_index_word = statement.text.rfind(word)
            end_index_word = start_index_word + len(word)
            right_sentence = statement.text[end_index_word:-1]
            near_operator = find_near_operator(word, right_sentence)
            if near_operator is not None:
                return "operator", near_operator, "divisory_proximity"
    for operator in operators_dictionary.keys():
        if operator in statement.text:
            word_type = "operator"
            if operator in operators_left_dictionary_to_delegate_add_substract.keys():
                word_type = "operator_left_delegate_add_substract"
            elif operator in operators_left_dictionary.keys():
                word_type = "operator_left"
            elif operator in operators_right_dictionary.keys():
                word_type = "operator_right"
            return word_type, operator, "secondary_order"
    # Si no salio por encontrar ningun operador, busco numero o incognita
    for token in statement:
        if token.pos_ == "NUM" or token.text.isnumeric():
            if token.text.isnumeric():
                return "leaf", token.text, "last_order"
            if string_is_numeric(token.text):
                return "leaf", token.text, "last_order"
            else:  # Es un numero en palabras
                number = recognize_number(token.text, Culture.Spanish)[0].resolution["value"]
                return "leaf", number, "last_order"
    else:
        return "leaf", "x", "last_order"  # TODO


class Node:

    def __init__(self, sentence):
        word_type, word, order = search_math_term(sentence)
        if word_type == "operator":
            # Si es de 1er orden, puede estar el caso de "mayor o igual" que quiero quedarme con toda la expresion
            if order == "first_order":
                value = word
            else:  # Si hay un "y multiplicado" yo solo quiero tomar el ultimo (multiplicado)
                value = word.split()[-1]
            operator = operators_dictionary[value]  # Busco el operador que se corresponde con la palabra
            parts_of_sentence = sentence.split(word)
            parts_number = len(parts_of_sentence)
            if parts_number > 2:  # Al splitear encontro mas de una ocurrencia
                first_part_after_split = word.join(parts_of_sentence[:-1])  # Joineo todas las partes excepto la ultima
                last_part_after_split = parts_of_sentence[parts_number - 1]
                self.operator = operator
                self.left_node = Node(first_part_after_split)
                self.right_node = Node(last_part_after_split)
            else:
                self.operator = operator
                self.left_node = Node(parts_of_sentence[0])
                self.right_node = Node(parts_of_sentence[1])
        # Casos operadores especiales
        elif word_type == "operator_left_delegate_add_substract":  # Sumatoria de 5 y 5"
            parts_of_sentence = sentence.split(word)
            self.operator = "(" + addSubstractInterpreter.translate_statement(word + parts_of_sentence[1],
                                                                              "equation").expression + ")"
            self.left_node = None
            self.right_node = None
        elif word_type == "operator_left":  # Si tengo un caso como "el triple de 2"
            parts_of_sentence = sentence.split(word)
            self.operator = operators_left_dictionary[word]
            self.left_node = None
            self.right_node = Node(parts_of_sentence[1])
        elif word_type == "operator_right":  # Si tengo un caso como "2 triplicado"
            parts_of_sentence = sentence.split(word)
            self.operator = operators_right_dictionary[word]
            self.left_node = Node(parts_of_sentence[0])
            self.right_node = None
        else:
            self.operator = word
            self.left_node = None
            self.right_node = None

    def resolve(self):
        if self.left_node is None and self.right_node is None:
            return self.operator
        elif self.left_node is None and self.right_node is not None:  # Si tengo un caso como "el doble de 2"
            return "(" + self.operator + " " + self.right_node.resolve() + ")"
        elif self.left_node is not None and self.right_node is None:  # Si tengo un caso como "2 duplicado"
            return "(" + self.left_node.resolve() + " " + self.operator + ")"
        else:
            return "(" + self.left_node.resolve() + " " + self.operator + " " + self.right_node.resolve() + ")"


def translate_statement(statement, tag):
    p1 = Node(statement)
    result = p1.resolve()
    final_result = result[1:-1]
    if not any(word in first_order_operators_dictionary.values() for word in final_result):
        final_result = final_result + " = x"
    return Response(final_result, tag)
