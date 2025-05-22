from flask import Flask, request, jsonify
import os

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
    port = int(os.environ.get('PORT', 5000))  # Required for Render
    app.run(host='0.0.0.0', port=port)
