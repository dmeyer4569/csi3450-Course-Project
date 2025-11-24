# csi3450-Course-Project

CRUD Course Project for CSI3450 Database class.

we use sqlite for local testing and will probably end up as our main database. 
SQlite is a great and lightweight RDBMS. The only difference between SQLite databases and MySQL/MariaDB/PostgreSQL/Oracle is that SQLite doesn't run as a seperate process. Instead it runs as part of the application using it. 

The current Diagram, might change
![alt text](diagram.png)

# How to use this app

Start by creating a venv, then install all requirements from requirements.txt (Note this might require some manual library installation depending on the OS you use. macOS has different library names for some)

    > pip install -r requirements.txt

First enter the backend directory and start fastAPI
    
    > cd backend
    > fastapi dev main.py

Now you can access all currently existent endpoints by going to

    > http://127.0.0.1:8000/docs#/

Next start the frontend

To be complete