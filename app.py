from flask import Flask, request
import sqlite3
import threading

app = Flask(__name__)

local_db = threading.local()

def get_db():
    # Check if the thread-local object has a database connection
    if not hasattr(local_db, 'conn'):
        # If not, create a new database connection
        local_db.conn = sqlite3.connect('goober_value.db')

    # Return the database connection from the thread-local object
    return local_db.conn

# create table if not exists
db = get_db()
db.execute('CREATE TABLE IF NOT EXISTS goober_value (value TEXT)')
db.execute('INSERT OR IGNORE INTO goober_value (value) VALUES (?)', ('',))
db.commit()

@app.route('/', methods=['GET'])
def goober_value():

    db = get_db()

    # Check if the request includes a query string parameter named "goober"
    if 'goober' in request.args:
        # Update the goober value in the database
        value = request.args['goober']
        db.execute('UPDATE goober_value SET value = ?', (value,))
        db.commit()

    # Get the current goober value from the database
    cursor = db.execute('SELECT value FROM goober_value')
    value = cursor.fetchone()[0]

    # Return the goober value as a JSON response
    return {'goober': value}

if __name__ == '__main__':
    app.run()