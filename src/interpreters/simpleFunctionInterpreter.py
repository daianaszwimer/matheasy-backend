import re

from src.interpreters.domain import Response

init_characters = ["f", "x", "(", "{", "[", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
end_characters = [")", "}", "]", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pattern = re.compile(r"\s+")


def translate_statement(statement, tag):
    statement = statement.lower()
    init_index = search_character(init_characters, statement)
    end_index = len(statement) - search_character(end_characters, statement[::-1])
    equation = statement[init_index:end_index]
    # Normalizo los espacios en blanco de la ecuacion
    normalized_equation = pattern.sub("", equation)
    if "f(x)=" or "y=" in normalized_equation:
        normalized_equation = str(normalized_equation).replace('f(x)=', '')
        normalized_equation = str(normalized_equation).replace('y=', '')
    if "=f(x)" or "=y" in normalized_equation:
        normalized_equation = str(normalized_equation).replace('=f(x)', '')
        normalized_equation = str(normalized_equation).replace('=y', '')
    return Response(normalized_equation, tag)


def search_character(characters, statement):
    index = len(statement) + 1
    for character in characters:
        searched_indexes = [i for i, x in enumerate(statement) if x == character]
        for searched_index in searched_indexes:
            if searched_index < index and searched_index != -1 and following_characters_accepted(statement,
                                                                                                 searched_index):
                index = searched_index
    return index


def following_characters_accepted(statement, index):
    accepted_characters = [*init_characters, *end_characters, "(", "x", "[", "+", "-", "*", "/", "=", "^", " "]
    if index + 2 > len(statement) - 1:
        return True
    return statement[index + 1] in accepted_characters and statement[index + 2] in accepted_characters
