import src.interpreters.interpreter as interpreter
import src.modelPredictor as modelPredictor


def result(statement):
    # Si hay que hacer alguna limpieza del statement antes de llegar al predictor se hace aca
    # Limpiar tildes
    prediction = modelPredictor.predict(statement)
    equation = interpreter.interpret("ecuacion-implicita", statement)  # TODO: Modificar
    result = equation  # result = profebot.resolution(equation) -> TODO Cuando tengamos ProfeBot en el codigo
    return result
