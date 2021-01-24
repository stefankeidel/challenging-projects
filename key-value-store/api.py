from flask import Flask, make_response, request, jsonify


APP = Flask(__name__)
APP.config["DEBUG"] = True

RECORDS = {}

@APP.route("/", methods=["GET"])
def home():
    return """Hello, World"""


# A route to return key count
@APP.route("/api/v1/records", methods=["GET"])
def record_count():
    return jsonify({"count": len(RECORDS)})


@APP.route("/api/v1/record/<key>", methods=["PUT"])
def record_put(key):
    """Replaces or creates record"""

    req = request.get_json()

    if key in RECORDS:
        RECORDS[key] = req
        res = make_response(jsonify({"message": "Record replaced successfully"}), 200)
        return res

    RECORDS[key] = req
    res = make_response(jsonify({"message": "Record created successfully"}), 201)
    return res

@APP.route("/api/v1/record/<key>", methods=["GET"])
def record_get(key):
    """Returns record from memory"""

    if key in RECORDS:
        res = make_response(jsonify(RECORDS[key]), 200)
    else:
        res = make_response(jsonify({"message": "Record not found"}), 404)

    return res


APP.run()
