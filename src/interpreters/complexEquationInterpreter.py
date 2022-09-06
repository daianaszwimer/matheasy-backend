import spacy
from recognizers_number import recognize_number, Culture

# Subdivision del problema
# 1. Armado del arbol
#### 1a. Identificacion de los operadores segun prioridad
#### 1b. Me quedo del enunciado las partes matematicas
# 2. Resolucion del arbol -> DONE

# Operadores de 1er orden: = >= <= > <
# Operadores de 2do orden: + -
# Operadores de 3er orden: * / ¿^?

npl = spacy.load('es_core_news_lg')
# TODO: Ver como tomar el mayor o igual o menor o igual siendo varias palabras? -> Cargarlo al diccionario de spacy?
first_order_operators_dictionary = {"igual": "=", "mayor o igual": ">=", "menor o igual": "<=", "mayor": ">",
                                    "menor": "<"}
second_order_operators_dictionary = {"mas": "+", "menos": "-", "suma": "+", "resta": "-"}
third_order_operators_dictionary = {"por": "*", "dividido": "/", "multiplicacion": "*", "division": "/"}
operators_dictionary = {}
operators_dictionary.update(first_order_operators_dictionary)
operators_dictionary.update(second_order_operators_dictionary)
operators_dictionary.update(third_order_operators_dictionary)


def search_math_term(sentence):
    statement = npl(sentence)
    for operator in operators_dictionary.keys():
        if operator in statement.text:
            print("Encontre un operador en statement: " + operator)
            return "operator", operator
    # Si no salio por encontrar ningun operador, busco numero o incognita
    print("Voy a analizar si encuentro algun numero en: " + statement.text)
    for token in statement:
        print("Voy a analizar si esto es un numero: " + token.text)
        if token.pos_ == "NUM" or token.text.isnumeric():
            print("Encontre un numero: " + token.text)
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
            operator = operators_dictionary[word]  # Busco el operador que se corresponde con la palabra
            print("Tengo un operador que es: " + word + " y su simbolo es " + operator)
            parts_of_sentence = sentence.split(word)
            print("Las dos partes que me quedan despues de este operador, son: " + parts_of_sentence[0] + " // " +
                  parts_of_sentence[1])
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
            return self.left_node.resolve() + " " + self.operator + " " + self.right_node.resolve()


def translate_statement(statement):
    '''p1 = Node("¿Cual es el numero que sumado a 1 es igual a 2?")
    print(p1.resolve())
    return p1.resolve()'''
    p1 = Node(statement)
    print(p1.resolve())
    return p1.resolve()

# ¿Que falta?:
# spacy: contemplar mayor e igual, y eso
# detectar parentesis en el caso de un "y"