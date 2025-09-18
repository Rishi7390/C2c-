import os
import sqlite3
import shutil
import threading
import requests

# Function to download a file in background
def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

# Example URL (replace with your own file)
threading.Thread(target=download_file, args=("https://example.com/file.zip", "file.zip")).start()

# Safe SQLite example (works with your own DB)
db_path = "my_database.db"
shutil.copy2(db_path, "temp_db.db")
conn = sqlite3.connect("temp_db.db")
cursor = conn.cursor()

# Read data safely
cursor.execute("SELECT * FROM my_table")
for row in cursor.fetchall():
    print(row)

conn.close()
os.remove("temp_db.db")
