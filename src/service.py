import src.interpreters.interpreter as interpreter
import src.modelPredictor as modelPredictor
import src.mathgenerators.mathgenerator as mathgenerator
from src.utils import get_root_of_equation, get_exponent_of_equation

def result(statement):
    statement = statement.lower()
    prediction = modelPredictor.predict(statement)
    equation = interpreter.interpret(prediction, statement)
    return equation

def suggestions(equation, tag): 
    root = get_root_of_equation(equation)
    exponent = get_exponent_of_equation(equation).value
    exerciselist = []

    # Number of exercises to generate
    for _ in range(3):
        similarexercise = mathgenerator.generate_exercise(exponent, tag).replace("=", root)
        exerciselist.append(similarexercise)
    
    return exerciselist