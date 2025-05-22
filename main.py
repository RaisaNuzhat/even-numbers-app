from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/even" method="get">
            Enter a number: <input name="n" type="number">
            <input type="submit">
        </form>
    '''

@app.route('/even', methods=['GET'])
def generate_even():
    try:
        n = int(request.args.get('n', 0))
        even_numbers = [i for i in range(2, 2 * n + 1, 2)]
        return jsonify({"Even numbers": even_numbers})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
