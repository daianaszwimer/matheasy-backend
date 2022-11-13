import spacy
from recognizers_number import recognize_number, Culture
from src.interpreters.domain import Response

npl = spacy.load('es_core_news_lg') # TODO: Ver de hacerlo mas global

def translate_statement(statement, tag):
    def is_operator(token):
        return token.text in list(operators.keys())

    operators = {"suma": "+", "resta": "-", "sumar": "+", "restar": "-", "más": "+", "mas": "+", "menos": "-", "sumatoria": "+", "diferencia": "-"} # Aca deberia ir la palabra raiz nomas
    doc = npl(statement)
    mathProblem = []
    for token in doc:
        if token.pos_ == "NUM" or is_operator(token) or token.text.isnumeric():
            mathProblem.append(token)

    def translate(token):
      if is_operator(token):
        return (operators[token.text], token)
      else:
        return (token.text, token)

    translatedProblem = list(map(translate, mathProblem))
    finalTranslatedProblem = []
    for palabra, token in translatedProblem:
      if is_operator(token):
        operator = palabra
      else:
        if palabra.isnumeric():
            finalTranslatedProblem.append(palabra)
        else:
            result = recognize_number(palabra, Culture.Spanish)[0].resolution["value"]
            finalTranslatedProblem.append(result)
        finalTranslatedProblem.append(operator)
    finalTranslatedProblem.pop()
    equation = ' '.join(finalTranslatedProblem)
    return Response(equation, tag)