from flask import Blueprint, json, abort, request, redirect, url_for
import database_connection
from psycopg2 import errors
import logging


employee_bp = Blueprint('employee', __name__)


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
        with database_connection.connect() as connection:
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
@employee_bp.route('/', methods=['GET'])
@employee_bp.route('/employee/list', methods=['GET'])
def index():
    logging.info('Fetch employee list')
    logging.info('INFO LOG')
    return json.jsonify(get_employee_data())


@employee_bp.route('/<id>', methods=['GET'])
def details(id:int):
    logging.info('Fetch info for employee #{}'.format(id))
    data = get_employee_data(id)
    return abort(404) if 0 == len(data) else json.jsonify(data)


@employee_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    logging.info('Create employee using {}'.format(data))
    full_name = data.get('full_name').strip()
    if full_name is None:
        abort(400)

    status_code = data.get('status_code').strip()
    if status_code is None:
        abort(400)
    elif status_code not in ['enabled', 'disabled', 'suspended']:
        abort(400)

    try:
        with database_connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO employee(full_name, status_code) VALUES(%s,%s)', (full_name, status_code))
    except errors.InvalidTextRepresentation as err:
        logging.error('Encountered database error: "{}"'.format(err))
    return redirect(url_for('index'))


@employee_bp.route('/<id>', methods=['PUT'])
def update(id:int):
    data = request.get_json()
    logging.info('update employee #{} using {}'.format(id, data))
    full_name = data.get('full_name').strip()
    if full_name is None:
        abort(400)

    status_code = data.get('status_code').strip()
    if status_code is None:
        abort(400)
    elif status_code not in ['enabled', 'disabled', 'suspended']:
        abort(400)

    try:
        with database_connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE employee SET full_name=%s, status_code=%s WHERE id=%s', (full_name, status_code, id))
    except errors.InvalidTextRepresentation as err:
        logging.error('Encountered database error: "{}"'.format(err))
    return redirect(url_for('index'))    


@employee_bp.route('/<id>', methods=['DELETE'])
def delete(id:int):
    logging.info('delete employee #{}'.format(id))
    try:
        with database_connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM employee WHERE id=%s', (id))
    except errors.InvalidTextRepresentation as err:
        logging.error('Encountered database error: "{}"'.format(err))
    return redirect(url_for('index'))    

