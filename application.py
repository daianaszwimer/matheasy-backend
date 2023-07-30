from flasgger import swag_from, Swagger
from flask import Flask, request, jsonify

from src.modelTrainer import model, X_train, y_train
from src.utils import is_valid_statement

app = Flask(__name__)
swagger = Swagger(app)

import src.service as service

if __name__ == '__main__':
    app.run(port=8000)

@app.before_first_request
def before_first_request():
    model.fit(X_train, y_train)

@app.route('/', methods=["GET"])
@swag_from('./config/swagger.yml')
def helloworld():
    return jsonify('Ok!')


@app.route('/api/math-translation', methods=["POST"])
@swag_from('./config/swagger.yml')
def mathtranslation():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    input_json = request.get_json()  # get the json from the request

    text = input_json['text']
    # FIXME
    if not is_valid_statement(text):
        print(is_valid_statement(text))
        return jsonify({"error": "Invalid input - A mathematical statement is required"}), 400

    try:
        result = service.result(text)
        print(
            "La expresion matematica del enunciado: " + text + " es: " + result.expression + " y su tag es: " + result.tag)
        json = {"result": {"tag": result.tag, "expression": result.expression}}
        return jsonify(json)
    except:
        print("Error con el enunciado: ", text)
        return jsonify({"error": "An exception occurred"}), 404

@app.route('/api/suggestions', methods=["POST"])
@swag_from('./config/swagger.yml')
def suggestions():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    input_json = request.get_json()  # get the json from the request

    equation = input_json['equation']
    tag = input_json['tag']

    try:
        result = service.suggestions(equation, tag)
        return jsonify(result)
    except:
        return jsonify({"error": "An exception occurred"}), 404
