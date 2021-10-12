from flask import Flask, jsonify, request
import names_ages
# from names_ages import add_name_age, sfdfgdfg

APP = Flask(__name__)

@APP.route('/hello', methods=['GET'])
def hello():
    return "Hello1"

@APP.route('/getpeople', methods=['GET'])
def getpeople():
    min_age = int(request.args.get("min_age", 0))
    return jsonify(names_ages.get_names_ages(min_age))

@APP.route('/addperson', methods=['POST'])
def addperson():
    body = request.get_json()
    names_ages.add_name_age(body["name"], body["dob"])
    return {}

@APP.route('/clear', methods=['DELETE'])
def clear():
    names_ages.clear_names_ages()
    return {}


if __name__ == "__main__":
    APP.run(debug=True, port=8080)
