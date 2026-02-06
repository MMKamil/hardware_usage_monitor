import csv
import sqlite3
import os

DB_PATH = "sessions.db"

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
csv_path = os.path.join(desktop_path, "usage_log.csv")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT * FROM usage_log")
rows = cur.fetchall()
headers = [desc[0] for desc in cur.description]

conn.close()

with open(csv_path, 'w', newline='', encoding = "utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("CSV zapisany na pulpicie: ", csv_path)
