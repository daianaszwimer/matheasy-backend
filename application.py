from asyncio.log import logger
from flasgger import swag_from, Swagger
from flask import Flask, request, jsonify
from src.modelTrainer import model, X_train, y_train
import watchtower, logging
application = Flask(__name__)
swagger = Swagger(application)

logging.basicConfig(level=logging.INFO)
handler = watchtower.CloudWatchLogHandler(log_group_name=application.name)
application.logger.addHandler(handler)

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
        logger.info("La expresion matematica del enunciado: " + text + " es: " + result.expression + " y su tag es: " + result.tag)
        json = {"result": {"tag": result.tag, "expression": result.expression}}
        return jsonify(json)
    except:
        logger.info("Error con el enunciado: ", text)
        return jsonify({"error": "An exception occurred"}), 404
