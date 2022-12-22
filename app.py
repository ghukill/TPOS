from flask import Flask, request, jsonify
import sqlite3
import threading
import time

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
    CREATE TABLE IF NOT EXISTS stairs (
        distance numeric,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """
)
db.execute("""INSERT OR IGNORE INTO stairs (distance) VALUES (?)""", (-1,))
db.commit()


@app.route("/stairs/distance", methods=["GET"])
def stairs_distance():

    t0 = time.time()

    # get thread safe db
    db = get_db()

    # Check if the request includes a query string parameter named "goober"
    if "distance" in request.args:
        distance = request.args["distance"]
        distance = float(distance)
        db.execute("insert into stairs (distance) values(?)", (float(distance),))  # overwrites only row
        db.commit()

    # Get the current distance from the database
    cursor = db.execute("select distance from stairs order by timestamp desc limit 1;")
    value = cursor.fetchone()[0]

    # Return the goober value as a JSON response
    print(f"elapsed: {time.time()-t0}")
    return jsonify({"distance": value})


if __name__ == "__main__":
    app.run()
