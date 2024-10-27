
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/add" method="post">
        <input type="number" name="num1" placeholder="First Number" required>
        <input type="number" name="num2" placeholder="Second Number" required>
        <button type="submit">Add</button>
    </form>
    '''

@app.route('/add', methods=['POST'])
def add_numbers():
    num1 = request.form['num1']
    num2 = request.form['num2']
    result = float(num1) + float(num2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
