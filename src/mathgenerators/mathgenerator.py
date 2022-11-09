import src.mathgenerators.equationgenerator as equationgenerator
import src.mathgenerators.functiongenerator as functiongenerator
from src.enums import Tag

def generate_exercise(exponent, tag):
    if tag == Tag.Function.value:
        return functiongenerator.generate_equation(exponent)
    else:
        return equationgenerator.generate_equation(exponent)