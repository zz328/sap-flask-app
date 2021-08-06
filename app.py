from flask import Flask, abort, render_template

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71])
largestPrime = 71

#app root
@app.route("/")
def index():
    return "Welcome to the root page"

@app.route("/<number>/<option>")
def print_numbers(number, option):
    if (option != "odd") and (option != "even") and (option != "prime"):
        abort(404, description="Page not found");

    result = ''

    for i in range(1, int(number)+1):
        if (option == 'odd' and isOdd(i)) or (option == 'even' and isEven(i)) or (option == "prime" and isPrime(i)):
            result += str(i) + ' '

    return result

def isPrime(number):
    global largestPrime
    if number <= largestPrime:
        if number in primes:
            return True
        else:
            return False

    i = 2
    while (i * i <= number):
        if number % i == 0:
            return False
    
    primes.add(number)
    largestPrime = number
    return True

def isEven(number):
    return (number % 2 == 0)

def isOdd(number):
    return (number % 2 == 1)




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
