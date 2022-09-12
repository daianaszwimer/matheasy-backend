from flasgger import swag_from, Swagger
from flask import Flask, request, jsonify

from src.modelTrainer import model, X_train, y_train

application = Flask(__name__)
swagger = Swagger(application)

import src.service as service


@application.before_first_request
def before_first_request():
    model.fit(X_train, y_train)


@application.route('/', methods=["GET"])
@swag_from('./config/swagger.yml')
def helloworld():
    return jsonify('Hello World!')


@application.route('/api/ping', methods=["GET"])
@swag_from('./config/swagger.yml')
def pingpong():
    return jsonify('pong')


@application.route('/api/math-translation', methods=["POST"])
@swag_from('./config/swagger.yml')
def mathtranslation():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    input_json = request.get_json()  # get the json from the request

    text = input_json['text']

    try:
        result = service.result(text)
        json = {"result": {"tag": result.tag, "expression": result.expression}}
        return jsonify(json)
    except:
        return jsonify({"error": "An exception occurred"}), 404
