from flask import Flask, abort, render_template

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

#app root
@app.route("/")
def index():
    return "Welcome to the root page"

#shows odd or even numbers within the range
@app.route("/<number>/<isOdd>")
def print_numbers(number, isOdd):
    # goes to page not found if user didn't have odd or even in path
    if (isOdd != "odd") and (isOdd != "even"):
        abort(404, description="Page not found");

    result = ''

    for i in range(1, int(number)+1):
        if (isOdd == 'odd' and i % 2 == 1) or (isOdd == 'even' and i%2 == 0):
            result += str(i) + ' '

    return result

# shows numbers 1-number 
@app.route("/<number>")
def print_all_numbers(number):
    result = ''
    try:
        for i in range(1, int(number)+1):
            result += str(i) + ' '
    except:
        # if user did not put number in path
        abort(404, description="Page not found");

    return result

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
