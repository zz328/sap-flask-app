from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the root page"

@app.route("/<number>/<isOdd>")
def print_numbers(number, isOdd):
    if (isOdd != "odd") and (isOdd != "even"):
        abort(404, description="Page not found");

    result = ''

    for i in range(1, int(number)+1):
        if (isOdd == 'odd' and i % 2 == 1) or (isOdd == 'even' and i%2 == 0):
            result += str(i) + ' '

    return result

@app.route("/<number>")
def print_all_numbers(number):
    result = ''
    try:
        for i in range(1, int(number)+1):
            result += str(i) + ' '
    except:
        abort(404, description="Page not found");

    return result

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# main driver function
if __name__ == '__main__':
    app.run()