import spacy

# Subdivision del problema
# 1. Armado del arbol
#### 1a. Identificacion de los operadores segun prioridad
#### 1b. Me quedo del enunciado las partes matematicas
# 2. Resolucion del arbol -> DONE

# Operadores de 1er orden: = >= <= > <
# Operadores de 2do orden: + -
# Operadores de 3er orden: * / ¿^?

npl = spacy.load('es_core_news_lg')
# TODO: Ver como tomar el mayor o igual o menor o igual siendo varias palabras?
first_order_operators_dictionary = {"igual": "=", "mayor o igual": ">=", "menor o igual": "<=", "mayor": ">",
                                    "menor": "<"}
first_order_operators = ["=", ">=", "<=", ">", "<"]
second_order_operators_dictionary = {"mas": "+", "menos": "-", "suma": "+", "resta": "-"}
second_order_operators = ["+", "-"]
third_order_operators = ["*", "/"]


def translate_statement(statement):
    print("1. Traducir el enunciado: " + statement)
    equation_tree = []
    # Buscar first order operator en oracion (podria haber mas de uno? entiendo que no pq es la raiz)
    first_order_operator = None
    doc = npl(statement)
    for token in doc:
        if token.text in first_order_operators:
            first_order_operator = token.text
        if token.text in first_order_operators_dictionary.keys():
            first_order_operator = first_order_operators_dictionary[token.text]
            statement = statement.replace(token.text, first_order_operator)

    print("2. El operador de primer orden es: " + first_order_operator)
    operator_divisions = statement.split(first_order_operator)
    first_node = Node(first_order_operator, operator_divisions[0],
                      operator_divisions[1])  # Podria no existir el index 0 o 1?
    equation_tree.append(first_node)
    print("Operador: " + first_node.operator)
    print("Nodo izquierdo: " + first_node.left_node)
    print("Nodo derecho: " + first_node.right_node)

    # TODO: Lo que sigue deberia evaluarse multiples veces (buscando todos los de orden 2)
    # Evaluación del nodo izquierdo
    print("3. Evaluo el nodo izquierdo: " + first_node.left_node)
    second_order_operator = None
    doc2 = npl(first_node.left_node) # Aca me esta faltando "desechar" el string que ya se evaluo en el nodo anterior
    for token in doc2:
        if token.text in second_order_operators:
            second_order_operator = token.text
        if token.text in second_order_operators_dictionary.keys():
            second_order_operator = second_order_operators_dictionary[token.text]
            statement = statement.replace(token.text, second_order_operator)

    print("El primer operador de segundo orden es: " + second_order_operator)
    operator_divisions = statement.split(second_order_operator)
    second_node = Node(second_order_operator, operator_divisions[0], operator_divisions[1])
    equation_tree.append(second_node)
    print("Operador: " + second_node.operator)
    print("Nodo izquierdo: " + second_node.left_node)
    print("Nodo derecho: " + second_node.right_node)

    return equation_tree
    # Itero cada nodo del de arriba y busco operadores de 2do orden, podria haber muchos
    # Cuando termino con los de 2do orden, busco de 3er orden


class Node:
    def __init__(self, operator, left_node, right_node):
        self.operator = operator
        self.left_node = left_node
        self.right_node = right_node

    def resolve(self):
        # Existe un caso donde haya un hijo izquierdo en None y el otro no?
        if self.left_node is None and self.right_node is None:
            return self.operator
        else:
            return self.left_node.resolve() + " " + self.operator + " " + self.right_node.resolve()

# def translate_statement(statement):
#    p1 = Node("=", Node("+", Node("9", None, None), Node("8", None, None)), Node("3", None, None))
#    print(p1.resolve())
#    return p1.resolve()
