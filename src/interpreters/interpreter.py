import src.interpreters.addSubstractInterpreter as addSubstractInterpreter
import src.interpreters.simpleEquationInterpreter as simpleEquationInterpreter
import src.interpreters.complexEquationInterpreter as complexEquationInterpreter


def interpret(prediction, statement):
    if prediction == "suma" or prediction == "resta":
        return addSubstractInterpreter.translate_statement(statement)
    if prediction == "ecuacion-explicita":
        return simpleEquationInterpreter.translate_statement(statement)
    if prediction == "ecuacion-implicita":
        return complexEquationInterpreter.translate_statement(statement)
    else:  # TODO poner los demas interpreters
        return "ecuacion default"
