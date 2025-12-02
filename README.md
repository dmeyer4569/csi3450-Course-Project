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


# What endpoints exist

#### GET (Select)

 * Get Manufacturers
   * Returns the manufacturer details + logo
 * Get Cars
   * Returns a set amount of cars + first image
 * Get cars of a manufacturer
   * Returns all cars a manufacturer has
   * Returns the manufacturer logo
   * Returns the first car image of each car
   * Can be sorted by car year ascending/descending
   * Can be sorted by car MSRP ascending/descending
 * Get Images for a Car
   * Returns all car data + all images with a car

#### POST (Insert)

 * Spawn all the tables into a fresh new sqlite instance (highly doubt I'll change this to a different DB)
 * Insert all data into said tables (make sure to spawn tables before inserting data)
 * Insert a new manufacturer
   * When inserting a new manufacturer you can also upload the logo
 * Insert a new car
   * When inserting a car you can upload multiple images for the car image gallery

#### PUT (Edit)

 * Edit an existent manufacturer
 * Edit an existent car
 * Edit images associated with each (To be complete)

#### DELETE (Delete)

 * Delete a manufacturer
   * Cascades all images, cars, and car images related to manufacturer
 * Delete a car
   * Deletes all images associated with the car
 * Delete a image
   * Deletes a singular image (why? idk)