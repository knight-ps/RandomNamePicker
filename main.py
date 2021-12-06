from flask import Flask, render_template, request
import random
import datetime



app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)






@app.route('/index', methods=['GET', 'POST'])
def save_names():
    if request.method == "POST":
        receive = request.form["author"]
        names = receive.split(",")
        x = len(names)
        outcome = (names[random.randint(0, x - 1)])
        return render_template("winner.html", outcome=outcome)












if __name__ == "__main__":
    app.run(debug=True)
