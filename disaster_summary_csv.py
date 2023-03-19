import csv
import os
from pathlib import Path
import sqlite3
conn = sqlite3.connect('disaster_summary.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS summary')
print("table dropped successfully")
conn.execute('CREATE TABLE summary (Dis_ID INTEGER, Year INTEGER, Disaster_Group TEXT, Disaster_Type TEXT, Country TEXT, ISO TEXT, Total_Affected INTEGER, Total_Damages REAL)')
print("table created successfully")

with open('nartural_disasters_information/disasters_summary.csv', newline='') as f:
    reader = csv.reader(f,delimiter=',')
    next(reader)
    for row in reader:
        print(row)

        Dis_ID = (row[0])
        Year = (row[1])
        Disaster_Group = (row[2])
        Disaster_Type = (row[3])
        Country = row[4]
        ISO = row[5]
        Total_Affected = row[6]
        Total_Damages = row[7]

        cur.execute('INSERT INTO summary VALUES (?,?,?,?,?,?,?,?)',(Dis_ID, Year, Disaster_Group, Disaster_Type, Country, ISO, Total_Affected,Total_Damages))
        conn.commit()
    print("data parsed successfully");

    conn.close()