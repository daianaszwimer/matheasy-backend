import re

from src.interpreters.domain import Response

init_characters = ["(", "{", "[", "f", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
end_characters = [")", "}", "]", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pattern = re.compile(r"\s+")


# Si no arranca con f(x) se le agrega -> Mejorar

def translate_statement(statement, tag):
    statement = statement.lower()
    init_index = search_character(init_characters, statement) - 1  # TODO: Revisar
    end_index = len(statement) - search_character(end_characters, statement[::-1])
    equation = statement[init_index:end_index]
    if (not "f(x)" in equation and not "y =" in equation) or not "=" in equation:
        equation = "f(x) = " + str(equation)
    # Normalizo los espacios en blanco de la ecuacion
    normalized_equation = pattern.sub("", equation)
    return Response(normalized_equation, tag)


def search_character(characters, statement):
    index = len(statement) + 1
    for character in characters:
        searched_index = statement.find(character)
        if searched_index < index and searched_index != -1 and following_characters_accepted(statement, searched_index):
            index = searched_index
    return index


# Si viene algo como "Despeja x de tal ecuacion (...)" veo que el proximo caracter sea un caracter aceptado
def following_characters_accepted(statement, index):
    accepted_characters = [*init_characters, *end_characters, "(", "x", "[", "+", "-", "*", "/", "=", "^", " "]
    return statement[index + 1] in accepted_characters and statement[index + 2] in accepted_characters
