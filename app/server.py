from flask import Flask, json, abort
from psycopg2 import connect, extensions, errors
import logging

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1048576
app.config.from_prefixed_env()
logging.basicConfig(filename='/var/log/flask-app.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

def database_connection() -> extensions.connection:
    """Open a database connection."""
    return connect(
        host=app.config['DATABASE']['host'],
        database=app.config['DATABASE']['database'],
        user=app.config['DATABASE']['user'],
        password=app.config['DATABASE']['password'],
    )

def get_employee_data(id:int=None) -> list:
    """Get employee data from datbase."""
    logging.info('Query database')
    data = []
    if id is None:
        params = ()
        query = 'SELECT * FROM public.employee'
    else:
        params = (id)
        query = 'SELECT * FROM public.employee WHERE id=%s'

    try:
        with database_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            data = []
            for emp in cursor.fetchall():
                data.append({
                    'id': emp[0],
                    'full_name': emp[1],
                    'status_code': emp[2],
                })
    except errors.InvalidTextRepresentation as err:
        logging.error('Encountered database error: "{}"'.format(err))
    
    return data;

# ================================================================
# Define site routes.
# ================================================================
@app.route('/', methods=['GET'])
@app.route('/employee/list', methods=['GET'])
def index():
    logging.info('Fetch employee list')
    logging.info('INFO LOG')
    return json.jsonify(get_employee_data())

@app.route('/employee/<id>', methods=['GET'])
def details(id:int):
    logging.info('Fetch info for employee #{}'.format(id))
    data = get_employee_data(id)
    return abort(404) if 0 == len(data) else json.jsonify(data)


# ================================================================
# Execute app if ran directly.
# ================================================================
if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')