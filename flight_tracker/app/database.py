#!/bin/bash/python3

import sqlite3

#Initializing the SQLite database with flights table
def init_db():
    conn = sqlite3.connect('flights.db') #Conneting to database file
    cursor = conn.cursor()

    #Creating the flights table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT,
            altitude REAL,
            speed REAL,
            heading REAL,
            latitude REAL,
            longitude REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

