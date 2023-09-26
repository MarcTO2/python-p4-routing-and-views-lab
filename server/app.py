#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/parameter<string:param>')
def print_string(param):
    # This prints the string to the console 
    print(param)

    # Displays the parameter to the web browser
    return f"The parameter is: {param}"

@app.route('/count/parameter<int:num>')
def count(num):
    # Ensure the parameter is a positive integer
    if num < 1:
        return "Parameter must be a positive integer"

    # We generate a list of numbers in a specified range
    number = list(range(1, num + 1))

    # We create a sting with numbers
    numbers_string = '/n'.join(map(str, number))

    return numbers_string

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    # Check for division by zero
    if num2 == 0:
        abort(400, "Invalid operation")
        result = num1 / num2
    elif operation == '%"':
        result = num1 % num2
    else: 
        abort(400, "Invalid operation")

    return f"Result: {result}"




    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
