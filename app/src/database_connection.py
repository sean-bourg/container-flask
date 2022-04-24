import psycopg2 

host = None
database = None
user = None
password = None

def connect() -> psycopg2.extensions.connection:
    """Open a database connection."""
    global host, database, user, password
    return psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
    )
