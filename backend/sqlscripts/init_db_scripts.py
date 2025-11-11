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