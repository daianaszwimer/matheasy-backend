import src.interpreters.addSubstractInterpreter as addSubstractInterpreter
import src.interpreters.complexEquationInterpreter as complexEquationInterpreter
import src.interpreters.complexFunctionInterpreter as complexFunctionInterpreter
import src.interpreters.simpleEquationInterpreter as simpleEquationInterpreter
import src.interpreters.simpleFunctionInterpreter as simpleFunctionInterpreter
from src.interpreters.domain import Response


def interpret(prediction, statement):
    if prediction == "suma" or prediction == "resta":
        return addSubstractInterpreter.translate_statement(statement, "Equation")
    if prediction == "ecuacion-explicita":
        return simpleEquationInterpreter.translate_statement(statement, "Equation")
    if prediction == "ecuacion-implicita":
        return complexEquationInterpreter.translate_statement(statement, "Equation")
    if prediction == "funcion-explicita":
        return simpleFunctionInterpreter.translate_statement(statement, "Function")
    if prediction == "funcion-implicita":
        return complexFunctionInterpreter.translate_statement(statement, "Function")
    else:  # TODO poner los demas interpreters
        return Response("ecuacion default", "Equation")
