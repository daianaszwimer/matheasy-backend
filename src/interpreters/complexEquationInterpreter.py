# Subdivision del problema
# 1. Armado del arbol
#### 1a. Identificacion de los operadores segun prioridad
#### 1b. Me quedo del enunciado las partes matematicas
# 2. Resolucion del arbol -> DONE

# Operadores de 1er orden: = >= <= > <
# Operadores de 2do orden: + -
# Operadores de 3er orden: * / ¿^?

# Tener en cuenta que tambien van a venir en palabras (la mayoria de las veces) - falta mapear esto
first_order_operators = ["=", ">=", "<=", ">", "<"]
second_order_operators = ["+", "-"]
third_order_operators = ["*", "/"]


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


def translate_statement(statement):
    p1 = Node("=", Node("+", Node("9", None, None), Node("8", None, None)), Node("3", None, None))
    print(p1.resolve())
    return p1.resolve()
