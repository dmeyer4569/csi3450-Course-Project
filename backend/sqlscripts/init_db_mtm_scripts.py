from sqlalchemy import text    
# MovieProducer
create_movie_producer_table = text(
    """
    CREATE TABLE IF NOT EXISTS movieProducer (   
        movieID INT,
        producerID INT,
        PRIMARY KEY (movieID, producerID),
        FOREIGN KEY (movieID) REFERENCES Movie(movieID),
        FOREIGN KEY (producerID) REFERENCES Producer(producerID)
    )
    """
)
# MovieActor
create_movie_actor_table = text(
    """
    CREATE TABLE IF NOT EXISTS movieActor (
        movieID INT,
        actorID INT,
        PRIMARY KEY (movieID, actorID),
        FOREIGN KEY (movieID) REFERENCES Movie(movieID),
        FOREIGN KEY (actorID) REFERENCES Actor(actorID)
    )
    """
)
#  MovieActress
create_movie_actress_table = text(
    """
    CREATE TABLE IF NOT EXISTS movieActress (
        movieID INT,
        actressID INT,
        PRIMARY KEY (movieID, actressID),
        FOREIGN KEY (movieID) REFERENCES Movie(movieID),
        FOREIGN KEY (actressID) REFERENCES Actress(actressID)
    )
    """
)
# MovieWriter
create_movie_writer_table = text(
    """
    CREATE TABLE IF NOT EXISTS movieWriter (
        movieID INT,
        writerID INT,
        PRIMARY KEY (movieID, writerID),
        FOREIGN KEY (movieID) REFERENCES Movie(movieID),
        FOREIGN KEY (writerID) REFERENCES Writer(writerID)
    )
    """
)
# MovieDirector
create_movie_director_table = text(
    """
    CREATE TABLE IF NOT EXISTS movieDirector (
        movieID INT,
        directorID INT,
        PRIMARY KEY (movieID, directorID),
        FOREIGN KEY (movieID) REFERENCES Movie(movieID),
        FOREIGN KEY (directorID) REFERENCES Director(directorID)
    )
    """
)