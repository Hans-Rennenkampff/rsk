
from flask import Flask, render_template, url_for, request,Response
app = Flask(__name__)
css=[{"url": "Style"}]
name="fs"
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/process_data/', methods=['POST'])
def doit():
    index = request.form['index']

    # ... обработать данные ...
if __name__ == '__main__':
    app.run(debug=True)
    doit()
