import sqlite3,datetime
connection = sqlite3.connect("movie.db")
connection.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

CREATES = """CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT, release_date REAL, watched INTEGER);
"""
adds = "INSERT INTO movies (title,release_date,watched) VALUES(?,?,0);"
all_movies = "SELECT * FROM movies;"
future_movies = "SELECT * FROM movies WHERE release_date > ?;"
updates_watched = "UPDATE movies SET watched = 1 WHERE id = ?;"
get_watched_movies = "SELECT * FROM movies WHERE watched = 1;"
unwatched_movies = "SELECT * FROM movies WHERE watched = 0;"
delete_movies = "DELETE FROM movies WHERE id = ?;"

def create():
    connection.execute(CREATES)
    connection.commit()

def add(title,release_date):
    with connection:
      connection.execute(adds,(title,release_date,))

def display_movie(upcoming=False):
    cursor = connection.cursor()
    if upcoming:
        today_timestamp = datetime.datetime.today().timestamp()
        cursor.execute(future_movies,(today_timestamp,))
    else:
        cursor.execute(all_movies)
    return cursor.fetchall()

def update_watched(id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(updates_watched,(id,))

def get_watched_movie():
        cursor = connection.cursor()
        cursor.execute(get_watched_movies)
        return cursor.fetchall()
    
def unwatched_movie():
    with connection:
        cursor = connection.cursor()
        cursor.execute(unwatched_movies)
        return cursor.fetchall()

def delete_movie():
    with connection:
        cursor = connection.cursor()
        cursor.execute(delete_movies)
        return cursor.fetchall()
    
def search_movie(search):
    with connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM movies WHERE title LIKE '%{search}%'")
        return cursor.fetchall()