import os
import oracledb
from dotenv import load_dotenv
import csv

load_dotenv()

user = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")

dsn = oracledb.makedsn("localhost", 1522, service_name="stu")

connection = oracledb.connect(
    user=user,
    password=password,
    dsn=dsn
)

cursor = connection.cursor()

print("Connected to Oracle")

# TODO: add methods for setting up other tables

def setup_mit():
    # Drop table if it exists
    try:
        cursor.execute("DROP TABLE mit")
        print("Dropped existing MIT table")
    except oracledb.DatabaseError:
        print("MIT table did not exist")

    # Purge recycle bin
    cursor.execute("PURGE RECYCLEBIN")
    print("Recycle bin purged")

    # Create table
    cursor.execute("""
        CREATE TABLE mit (
            year NUMBER,
            state VARCHAR2(50),
            state_po VARCHAR2(5),
            candidate VARCHAR2(100),
            party VARCHAR2(50),
            votes NUMBER,
            totalvotes NUMBER
        )
    """)
    print("MIT table created")

    # Insert CSV data
    rows = []

    with open(
        "../../cleaned_data/mit/mit_presidential_election_data.csv",
        newline="",
        encoding="utf-8",
    ) as f:
        reader = csv.DictReader(f)

        for r in reader:
            rows.append((
                int(r["year"]),
                r["state"],
                r["state_po"],
                r["candidate"],
                r["party"],
                int(r["votes"]),
                int(r["totalvotes"])
            ))

    cursor.executemany("""
        INSERT INTO mit
        (year, state, state_po, candidate, party, votes, totalvotes)
        VALUES (:1,:2,:3,:4,:5,:6,:7)
    """, rows)

    print("Inserted MIT data")


# Run the setup
setup_mit()

connection.commit()

cursor.close()
connection.close()
