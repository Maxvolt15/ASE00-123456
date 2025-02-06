from flask import Flask, request, make_response, jsonify
from datetime import date
import random, operator, time, hashlib

def create_header(X,response):
    value = random.randint(0,X)
    response.headers['exam'] = str(value)
    return value, response


def calc(X):
    return X

app = Flask(__name__, instance_relative_config=True)

def create_value(X, r):
    a = create_header(X,r)[1].headers
    b = calc(X)
    a.set('exam', str(b))
    return a

def create_app():
    return app

def create_secret(X,response):
    example = date.today()
    ran, _ = create_header(X,response)
    b = create_value(X,response)
    b['exam'] = "0"+(b['exam'][::-1])
    password = hashlib.md5(b['exam'].encode()).hexdigest()
    response.headers['exan'] = example.strftime("%Y")+example.strftime("%m")+example.strftime("%d")
    response.set_cookie('exam', str(4*(ran+6)/2-ran*2))
    response.set_cookie('exan', password)
    return response

def get_input_and_compute(op, name):
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    if name == "*":
        time.sleep(1)
    return op(a,b)

@app.route('/add')
def add():
    value = get_input_and_compute(operator.add, "+")
    return make_response(jsonify(s=value), 200)
    
@app.route('/sub')
def sub():
    value = get_input_and_compute(operator.sub, "-")
    return make_response(jsonify(s=value), 200)

@app.route('/mul')
def mul():
    value = get_input_and_compute(operator.mul, "*")
    return make_response(jsonify(s=value), 200)

@app.route('/div')
def div():
    value = get_input_and_compute(operator.truediv, "/")
    return make_response(jsonify(s=value), 200)

@app.route('/mod')
def mod():
    value = get_input_and_compute(operator.mod, "%")
    return make_response(jsonify(s=value), 200)

@app.route('/secret', methods=['GET'])
def get_secret():
    X = request.args.get('X', type = int)
    response = make_response(jsonify(exam=X), 200)
    return create_secret(X,response)

#add your route here

@app.route('/ex1', methods=['GET'])
def ex1():
    X = request.args.get('a', type = str)
    D=0
    C=0
    for c in X:
        if c.isdigit():
            D+=1
        elif c.isalpha():
            C+=1

    if D == 0 or C == 0:
        return make_response(jsonify(s="invalid Input"),400)
    return make_response(jsonify(s=D//C),200)

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/ex1', methods=['GET'])
# def ex1():
#     # Get the query parameter 'a' from the request
#     X = request.args.get('a', type=str)

#     # If 'a' is not provided or is empty, return 400 with "Invalid Input"
#     if not X:
#         return jsonify(s="Invalid Input"), 400

#     # Count the number of digits (D) and alphabetic characters (C) in X
#     D = sum(c.isdigit() for c in X)  # Count digits
#     C = sum(c.isalpha() for c in X)  # Count alphabetic characters

#     # Check if the operation can be performed:
#     # - At least one digit must be present (D > 0)
#     # - Avoid division by zero (C > 0)
#     if D == 0 or C == 0:
#         return jsonify(s="Invalid Input"), 400

#     # Perform integer division D // C
#     result = D // C

#     # Return the result in JSON format with HTTP status 200
#     return jsonify(s=result), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)