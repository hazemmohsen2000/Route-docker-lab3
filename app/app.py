from flask import Flask
import mysql.connector
import redis

app = Flask(__name__)

@app.route('/')
def index():
    db = mysql.connector.connect(
        host='db',
        user='flaskuser',
        password='flaskpass',
        database='flaskdb'
    )
    r = redis.Redis(host='redis', port=6379)
    db_cursor = db.cursor()
    db_cursor.execute("SELECT NOW()")
    now = db_cursor.fetchone()
    r.set('last_access', str(now[0]))
    return f"Connected to MySQL and Redis! Time: {now[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
