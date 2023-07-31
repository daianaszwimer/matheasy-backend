from src.interpreters.domain import Response

# Es caracter de inicio si es -> ( o { o [ o incognita o numero
init_characters = ["x", "-", "(", "{", "[", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Es caracter de fin si es -> ) o }  o ] o incognita o numero
end_characters = [")", "}", "]", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def translate_statement(statement, tag):
    init_index = search_character(init_characters, statement)
    end_index = len(statement) - search_character(end_characters, statement[::-1])
    equation = statement[init_index:end_index]
    return Response(equation, tag)


def search_character(characters, statement):
    index = len(statement) + 1
    for character in characters:
        searched_indexes = [i for i, x in enumerate(statement) if x == character]
        for searched_index in searched_indexes:
            if searched_index < index and searched_index != -1 and following_characters_accepted(statement,
                                                                                                 searched_index):
                index = searched_index
    return index


# Si viene algo como "Despeja x de tal ecuacion (...)" veo que el proximo caracter sea un caracter aceptado
def following_characters_accepted(statement, index):
    accepted_characters = [*init_characters, *end_characters, "+", "-", "*", "/", "=", " ", ">", "<", "(", ")", "^"]
    if index + 2 > len(statement) - 1:
        return True
    return statement[index + 1] in accepted_characters and statement[index + 2] in accepted_characters
