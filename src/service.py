import src.interpreters.interpreter as interpreter
import src.modelPredictor as modelPredictor


def result(statement):
    statement = statement.lower()
    prediction = modelPredictor.predict(statement)
    equation = interpreter.interpret(prediction, statement)
    return equation
