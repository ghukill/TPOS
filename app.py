from flask import Flask, request, jsonify
import sqlite3
import threading

app = Flask(__name__)

local_db = threading.local()


def get_db():
    if not hasattr(local_db, "conn"):
        local_db.conn = sqlite3.connect("db/tpos.db")
    return local_db.conn


# run migrations
db = get_db()
db.execute(
    """
    CREATE TABLE IF NOT EXISTS garage (
        distance numeric
    );
    """
)
db.execute("""INSERT OR IGNORE INTO garage (distance) VALUES (?)""", (0.0,))
db.commit()


@app.route("/", methods=["GET"])
def goober_value():

    # get thread safe db
    db = get_db()

    # Check if the request includes a query string parameter named "goober"
    if "distance" in request.args:
        distance = request.args["distance"]
        db.execute("UPDATE garage SET distance = ?", (distance,))  # overwrites only row
        db.commit()

    # Get the current distance from the database
    cursor = db.execute("SELECT distance FROM garage")
    value = cursor.fetchone()[0]

    # Return the goober value as a JSON response
    return jsonify({"distance": value})


if __name__ == "__main__":
    app.run()
