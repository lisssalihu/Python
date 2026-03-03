import sqlite3

from Module19.main import title
from Module24.maiin import connection, cursor
from models import Moive , MovieCreate

def create_conection():
    """Create a database connection"""
    connection = sqlite3.connect("movie.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    """Create tables if they dont exist"""
    connection = create_conection()
    cursor = connection.cursor()
    cursor.execute("""
    Create Table IF DONT EXIST movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT NOT NULL)
    """)
    connection.commit()
    connection.close()


def create_movie(movie: MovieCreate) -> int:
    """
    ADDS a new movie to the database
    :param movie:
    Args:
    movie(MovieCreate)
    Return:
    int: The id of the new created movie
    :return:
    """
    connection = create_conection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO MOVIES (title , Director) Values(?,?)" , (movie.title , movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id


def read_movie():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * from movies")
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id=row[0] , title=row[1], director=row[2]) for row in row]
    return movies








