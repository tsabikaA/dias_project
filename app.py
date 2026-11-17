from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def splash():
    return render_template('splash.html')

@app.route('/main')
def home():
    return render_template('index11.html')
@app.route('/org')
def organogram():
    return render_template('orchart.html')

@app.route('/book')
def book_flight():
    food_menu = [
        {"id": 1, "name": "Ψητό Κοτόπουλο με πατάτες"},
        {"id": 2, "name": "Ζυμαρικά με λαχανικά"},
        {"id": 3, "name": "Ψάρι φιλέτο με ρούμι"},

    ]
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search_flights():
    departure = request.form.get('from')
    destination = request.form.get('to')
    date = request.form.get('date')
    all_flights = [
        {"flight_no": "DS401", "from": departure, "to": destination, 
        "time": "10:30", "price": "450$"},
        {"flight_no": "DS402", "from": departure, "to": destination,
         "time": "11:15", "price": "500$"}
    ]
    return render_template('results.html', flights=all_flights, 
        departure=departure, destination=destination, date=date)
if __name__ == '__main__':
    app.run(debug=True)