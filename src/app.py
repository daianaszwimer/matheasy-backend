from flask import Flask, request, jsonify
from flasgger import swag_from, Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/math-translation', methods=["POST"])
@swag_from('./config/swagger.yml')
def testpost():

    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    input_json = request.get_json() # get the json from the request
    
    text = input_json['text']

    return jsonify(text)