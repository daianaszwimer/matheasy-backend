from mathgenerator import mathgen
from src.enums import Exponent

def generate_equation(exponent):
    if exponent == Exponent.TWO.value:
        problem, solution = mathgen.quadratic_equation().replace("Zeros of the Quadratic Equation", "")
    else:
        problem, solution  = mathgen.basic_algebra()
    return problem