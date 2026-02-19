import sqlite3

conn = sqlite3.connect("favorites.db")

def init_db():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            user_id INTEGER,
            title TEXT
        )       
    """)
    conn.commit()
    
def get_favorites(user_id):
    cursor = conn.execute("SELECT title FROM favorites WHERE user_id = ?", (user_id,))
    return [row[0] for row in cursor.fetchall()]

def add_favorite(user_id, title):
    favorites = get_favorites(user_id)
    if len(favorites) >= 5:
        return "limit"
    if title in favorites:
        return "exists"
    conn.execute("INSERT INTO favorites VALUES (?, ?)", (user_id, title))
    conn.commit()
    return "ok"

def remove_favorite(user_id, title):
    conn.execute("DELETE FROM favorites WHERE user_id = ? AND title = ?", (user_id, title))
    conn.commit()