import spacy
from recognizers_number import recognize_number, Culture

from src.interpreters.domain import Response

npl = spacy.load('es_core_news_lg')
# TODO: Ver como tomar el mayor o igual o menor o igual siendo varias palabras? -> Cargarlo al diccionario de spacy?
first_order_operators_dictionary = {"igual": "=", "mayor o igual": ">=", "menor o igual": "<=", "mayor": ">",
                                    "menor": "<"}
dividing_words = ["y"]
dividing_by_proximity_words = [
    "todo esto ultimo"]  # TODO: El caso "y todo esto ultimo" me va a complicar, revisar como tomarlo
second_order_operators_dictionary = {"mas": "+", "menos": "-", "suma": "+", "sumado": "+", "resta": "-", "restado": "-"}
third_order_operators_dictionary = {"por": "*", "dividido": "/", "multiplicacion": "*", "division": "/",
                                    "multiplicado": "*"}  # TODO: multiplicado por
operators_dictionary = {}
operators_dictionary.update(first_order_operators_dictionary)
operators_dictionary.update(second_order_operators_dictionary)
operators_dictionary.update(third_order_operators_dictionary)


def find_near_operator(dividing_word, sentence):
    spliting_phrase = dividing_word
    statement = npl(sentence)
    for token in statement:
        if not token.text.isspace():
            spliting_phrase = spliting_phrase + " " + token.text
            if token.pos_ == "NUM" or token.text.isnumeric():
                return None
            if token.text in operators_dictionary.keys():
                return spliting_phrase


def search_math_term(sentence):
    statement = npl(sentence)
    for operator in first_order_operators_dictionary.keys():
        if operator in statement.text:
            return "operator", operator
    for word in dividing_words:
        if word in statement.text:
            start_index_word = statement.text.rfind(word)
            end_index_word = start_index_word + len(word)
            right_sentence = statement.text[end_index_word:-1]
            near_operator = find_near_operator(word, right_sentence)
            if near_operator is not None:
                return "operator", near_operator
    for word in dividing_by_proximity_words:
        if word in statement.text:
            start_index_word = statement.text.rfind(word)
            end_index_word = start_index_word + len(word)
            right_sentence = statement.text[end_index_word:-1]
            near_operator = find_near_operator(word, right_sentence)
            if near_operator is not None:
                return "operator", near_operator
    for operator in operators_dictionary.keys():
        if operator in statement.text:
            return "operator", operator
    # Si no salio por encontrar ningun operador, busco numero o incognita
    for token in statement:
        if token.pos_ == "NUM" or token.text.isnumeric():
            if token.text.isnumeric():
                return "leaf", token.text
            else:  # Es un numero en palabras
                number = recognize_number(token.text, Culture.Spanish)[0].resolution["value"]
                return "leaf", number
    else:
        return "leaf", "x"  # TODO


class Node:

    def __init__(self, sentence):
        word_type, word = search_math_term(sentence)
        if word_type == "operator":
            operator = operators_dictionary[word.split()[-1]]  # Busco el operador que se corresponde con la palabra
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
        else:
            self.operator = word
            self.left_node = None
            self.right_node = None

    def resolve(self):
        # Existe un caso donde haya un hijo izquierdo en None y el otro no?
        if self.left_node is None and self.right_node is None:
            return self.operator
        else:
            return "(" + self.left_node.resolve() + " " + self.operator + " " + self.right_node.resolve() + ")"


def translate_statement(statement, tag):
    p1 = Node(statement)
    result = p1.resolve()
    final_result = result[1:-1]
    if "funcion" in statement or tag == "Function":  # TODO: Mejorar
        return Response(final_result, tag)
    else:
        return Response(final_result, tag)
