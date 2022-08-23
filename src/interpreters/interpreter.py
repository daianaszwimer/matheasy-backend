import src.interpreters.addSubstractInterpreter as addSubstractInterpreter
import src.interpreters.simpleEquationInterpreter as simpleEquationInterpreter


def interpret(prediction, statement):
    if prediction == "suma" or prediction == "resta":
        return addSubstractInterpreter.translate_statement(statement)
    if prediction == "ecuacion":
        return simpleEquationInterpreter.translate_statement(statement)
    else:  # TODO poner los demas interpreters
        return "ecuacion default"
