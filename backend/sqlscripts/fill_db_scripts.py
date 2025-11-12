from sqlalchemy import text

insert_into_movie = text(
    """
    INSERT INTO movie (title, releaseDate, synopsis, rating, length, category)
    VALUES (:title, :releaseDate, :synopsis, :rating, :length, :category)
    """
)