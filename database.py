import sqlite3

DB_PATH = "sessions.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                duration REAL NOT NULL,
                avg_cpu REAL NOT NULL,
                avg_ram REAL NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usage_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                cpu REAL NOT NULL,
                ram REAL NOT NULL
            )
        """)
        conn.commit()
    finally:
        conn.close()


def save_session(start_time, end_time, duration, avg_cpu, avg_ram):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO sessions (
                start_time, end_time, duration, avg_cpu, avg_ram
            ) VALUES (?, ?, ?, ?, ?)
        """, (start_time, end_time, duration, avg_cpu, avg_ram))
        conn.commit()
    finally:
        conn.close()
def save_usage_log(timestamp, cpu, ram):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO usage_log (
            timestamp, cpu, ram
        ) VALUES (?, ?, ?)
    """, (timestamp, cpu, ram))
        conn.commit()
    finally:
        conn.close()


