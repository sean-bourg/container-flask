from flask import Flask, json, request
import logging

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1048576
app.secret_key = 'sample-application'
logging.basicConfig(filename='/tmp/app.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# ================================================================
# Define site routes.
# ================================================================


@app.route('/')
def index():
    return json.jsonify({
        "app": __name__,
        "func": "index",
        "args": request.args
    })

@app.route('/user/<id>')
def details(id:int):
    return json.jsonify({
        "app": __name__,
        "func": "index",
        "args": id
    })


# ================================================================
# Execute app if ran directly.
# ================================================================
if __name__ == "__main__":

    app.run(debug=True, port=8080, host='0.0.0.0')
