from flasgger import swag_from, Swagger
from flask import Flask, request, jsonify
import logging
from src.modelTrainer import model, X_train, y_train

application = Flask(__name__)
swagger = Swagger(application)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import src.service as service

@application.before_first_request
def before_first_request():
    model.fit(X_train, y_train)


@application.route('/', methods=["GET"])
@swag_from('./config/swagger.yml')
def helloworld():
    return jsonify('Ok!')

@application.route('/api/math-translation', methods=["POST"])
@swag_from('./config/swagger.yml')
def mathtranslation():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    input_json = request.get_json()  # get the json from the request

    text = input_json['text']

    try:
        result = service.result(text)
        logger.info("La traduccion del enunciado: " + text + " es: " + result)
        json = {"result": {"tag": result.tag, "expression": result.expression}}
        return jsonify(json)
    except:
        logger.info("Error con el enunciado: ", text)
        return jsonify({"error": "An exception occurred"}), 404
