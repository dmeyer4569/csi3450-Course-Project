from sqlalchemy import text
# Movie 
create_movie_table = text(
    """
    CREATE TABLE IF NOT EXISTS movie (
        movieID INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        releaseDate DATE,
        synopsis TEXT,
        rating INT,
        length TIME,
        category TEXT
    )
    """)

#producer
create_producer_table = text(
    """
    CREATE TABLE IF NOT EXISTS producer (
        producerID INTEGER PRIMARY KEY AUTOINCREMENT,
        position VARCHAR(25)
    )
    """
)
#actor
create_actor_table = text( 
    """
    CREATE TABLE IF NOT EXISTS actor (
        actorID INTEGER PRIMARY KEY AUTOINCREMENT,
        role VARCHAR(25)
    )
    """
)

#actreess
create_actress_table = text( 
    """
    CREATE TABLE IF NOT EXISTS actress (
        actressID INTEGER PRIMARY KEY AUTOINCREMENT,
        role VARCHAR(25)
    )
    """
)

# person
create_person_table = text(
    """
    CREATE TABLE IF NOT EXISTS person (
        personID INTEGER PRIMARY KEY AUTOINCREMENT,
        lastName VARCHAR(25),
        firsName VARCHAR(25),
        pay INT
    )
    """
)

# writer
create_writer_table = text(
    """
    CREATE TABLE IF NOT EXISTS writer (
        writerID INTEGER PRIMARY KEY AUTOINCREMENT,
        contribution TEXT
    )
    """
)

#Director 
create_director_table = text(
    """
    CREATE TABLE IF NOT EXISTS director (
        directorID INTEGER PRIMARY KEY AUTOINCREMENT,
        position VARCHAR(25)
    )
    """
)