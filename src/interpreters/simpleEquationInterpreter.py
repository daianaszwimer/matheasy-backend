import spacy

# Enunciado tramposo -> Despejar la x de la siguiente ecuacion: (x-4) + 3 = 2 sabiendo que la x es un numero mayor a 1
# Resolvé la ecuación: 3220 + x = 1127.
npl = spacy.load('es_core_news_lg')
# TODO: Interpretar todo el abecedario como posible incognita
# Es caracter de inicio si -> ( o { o [ o incognita o numero
init_characters = ["(", "{", "[", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Es caracter de fin si -> ) o }  o ] o incognita o numero
end_characters = [")", "}", "]", "x", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def translate_statement(statement):
    init_index = search_character(init_characters, statement)
    end_index = len(statement) - search_character(end_characters, statement[::-1])
    equation = statement[init_index:end_index]
    return equation


def search_character(characters, statement):
    index = len(statement) + 1
    for character in characters:
        searched_index = statement.find(character)
        if searched_index < index and searched_index != -1 and following_characters_accepted(statement, searched_index):
            index = searched_index
    return index


# Si viene algo como "Despeja x de tal ecuacion (...)" veo que el proximo caracter sea un caracter aceptado
def following_characters_accepted(statement, index):
    accepted_characters = [*init_characters, *end_characters, "+", "-", "*", "/", "=", " "]
    return statement[index + 1] in accepted_characters and statement[index + 2] in accepted_characters


'''def translate_statement(statement):
    # Buscar caracter inicio
    init_index = search_init_index(statement)
    # Buscar caracter fin
    # Obtener ecuacion de enunciado y retornar -> enunciado[caracter_inicio:caracter_fin]


    def is_init_character(character):
        return character in ["(", "{", "["] or character.isnumeric() or character.isalpha()

    def is_end_character(character):
        return character in [")", "}", "]"] or character.isnumeric() or character.isalpha()

    def search_init_index(statement):
        index = len(statement) + 1'''
