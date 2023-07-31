from mathgenerator import mathgen

def generate_equation(exponent):
    problem, solution  = mathgen.stationary_points(exponent)
    return problem