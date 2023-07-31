import unidecode

import src.interpreters.interpreter as interpreter
import src.mathgenerators.mathgenerator as mathgenerator
import src.modelPredictor as modelPredictor
from src.utils import get_root_of_equation, get_exponent_of_equation, fix_near_operators


def result(statement):
    statement = statement.lower()
    statement = unidecode.unidecode(statement)
    statement = fix_near_operators(statement)
    prediction = modelPredictor.predict(statement)
    equation = interpreter.interpret(prediction, statement)
    return equation


def suggestions(equation, tag):
    root = get_root_of_equation(equation)
    exponent = get_exponent_of_equation(equation).value
    exerciselist = []
    exerciseqty = 3

    # Number of exercises to generate
    for _ in range(exerciseqty):
        similarexercise = mathgenerator.generate_exercise(exponent, tag).replace("=", root)
        if similarexercise in exerciselist:
            retry = 0
            while similarexercise in exerciselist and retry < 3:
                similarexercise = mathgenerator.generate_exercise(exponent, tag).replace("=", root)
                retry += 1
        exerciselist.append(similarexercise)

    return exerciselist
