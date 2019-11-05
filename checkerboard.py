from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<up>/<side>')
def checker(up,side):
    return render_template('index.html', up = int(up), side = int(side))

if __name__ == "__main__":
    app.run(debug = True)