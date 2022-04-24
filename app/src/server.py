from flask import Flask, json, abort
import database_connection
from employee import employee_bp
import logging

app = Flask(__name__)
app.register_blueprint(
    employee_bp, 
    url_prefix='/employee'
)

# Configure app.
app.config['MAX_CONTENT_LENGTH'] = 1048576
app.config.from_prefixed_env()
database_connection.host=app.config['DATABASE']['host']
database_connection.database=app.config['DATABASE']['database']
database_connection.user=app.config['DATABASE']['user']
database_connection.password=app.config['DATABASE']['password']

# init logging.
logging.basicConfig(filename='/var/log/flask-app.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/')
def index():
    return json.jsonify(None)

# ================================================================
# Execute app if ran directly.
# ================================================================
if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')