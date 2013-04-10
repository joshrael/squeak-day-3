from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    search_term = request.form['term']
    location = request.form['location']
    numbers = range(10)
    return render_template('results.html',
                            search_term=search_term,
                            location=location,
                            numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
