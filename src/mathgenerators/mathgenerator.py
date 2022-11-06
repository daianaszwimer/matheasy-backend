import src.mathgenerators.equationgenerator as equationgenerator
import src.mathgenerators.functiongenerator as functiongenerator

def generate_exercise(equation, exponent):
    if "f(x)" in equation:
        return functiongenerator.generate_equation(exponent)
    else:
        return equationgenerator.generate_equation(exponent)