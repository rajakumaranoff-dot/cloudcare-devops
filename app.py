import os
import time
import psycopg
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB")
    )

def initialize_database():
    for attempt in range(10):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS cloudcare_status (
                            id SERIAL PRIMARY KEY,
                            message VARCHAR(255)
                        )
                    """)
                    cur.execute("""
                        INSERT INTO cloudcare_status (message)
                        VALUES (%s)
                    """, ("CloudCare connected to PostgreSQL!",))
            print("CloudCare database initialized successfully!")
            return
        except psycopg.OperationalError as error:
            print(f"Database not ready. Attempt {attempt + 1}/10")
            time.sleep(3)

    raise RuntimeError("Could not connect to PostgreSQL")

@app.route("/")
def home():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT message FROM cloudcare_status ORDER BY id DESC LIMIT 1"
                )
                result = cur.fetchone()

        database_status = result[0] if result else "No database record found"

    except psycopg.Error:
        database_status = "Database connection failed"

    return f"""
    <html>
        <head>
            <title>CloudCare DevOps</title>
        </head>
        <body>
            <h1>Welcome to CloudCare!</h1>
            <h2>My First DevOps Project</h2>
            <p>Application successfully deployed using Python Flask.</p>
            <p>Next stop: AWS Cloud Infrastructure!</p>
            <h3>Database Status: {database_status}</h3>
        </body>
    </html>
    """

if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5000, debug=False)