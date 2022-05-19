import psycopg2
import csv

# Connecting to the PostgreSQL database
try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="PC Games Sales",
        user="postgres",
        password="Felipe1998",
    )
    print("Succesfuly connected")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
conn.set_session(autocommit=True)

# cursor so excute SQL queries
db = conn.cursor()

# Creating the respective tables for the database
db.execute(
    """
    DROP TABLE IF EXISTS Games;

    CREATE TABLE Games (
        Id INTEGER NOT NULL PRIMARY KEY,
        Name TEXT,
        Sales_millions DECIMAL,
        Series TEXT,
        Release_date TEXT,
        Genre TEXT,
        Developer TEXT,
        Publisher TEXt
    );
"""
)
print("Table succesfully created")

# reading the csv file and adding the information to the database
with open("Games.csv", "r") as game_file:
    dict_reader = csv.DictReader(game_file)
    for id, row in enumerate(dict_reader, start=1):
        name = row["ï»¿Name"]
        sales = row["Sales"]
        series = row["Series"]
        release = row["Release"]
        genre = row["Genre"]
        developer = row["Developer"]
        publisher = row["Publisher"]
        # inserting the information in the db
        db.execute(
            """
            INSERT INTO Games (Id, Name, Sales_millions, Series, Release_date, Genre, Developer, Publisher)\
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (id, name, sales, series, release, genre, developer, publisher),
        )
print("info succesfully inserted")

# Validating the data is inserted into the tables

db.execute(
    """
    SELECT * FROM Games;
"""
)
while lines := db.fetchone():
    print(lines)
db.close()
conn.close()
