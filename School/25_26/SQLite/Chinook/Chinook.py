import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "chinook.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

query = """
SELECT albums.Title, artists.Name
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId;
"""

cur.execute(query)
rows = cur.fetchall()

for title, artist in rows:
    print(f"{title} — {artist}")

conn.close()