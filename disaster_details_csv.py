import csv
import os
from pathlib import Path
import sqlite3
conn = sqlite3.connect('disaster_details.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS details')
print("table dropped successfully")
conn.execute('CREATE TABLE details (Dis_ID INTEGER, '
             'Seq INTEGER, '
             'Disaster_Subgroup TEXT,'
             'Disaster_Subtype TEXT,'
             'Region TEXT, '
             'Continent TEXT, '
             'Location TEXT,'
             'OFDA_Response INTEGER,'
             'Appeal INTEGER,'
             'Declaration INTEGER,'
             'Local_Time TEXT,'
             'Start_Year INTEGER,'
             'Start_Month INTEGER,'
             'Start_Day INTEGER,'
             'End_Year INTEGER,'
             'End_Month INTEGER,'
             'End_Day INTEGER,'
             'Total_Deaths INTEGER,'
             'insured_damages_usd INTEGER,'
             'Total_Damages_usd INTEGER,'
             'CPI REAL)')
print("table created successfully")

with open('nartural_disasters_information/disasters_details.csv', newline='') as f:
    reader = csv.reader(f,delimiter=',')
    next(reader)
    for row in reader:
        print(row)

        Dis_ID = (row[0])
        Seq = (row[1])
        Disaster_Subgroup = (row[2])
        Disaster_Subtype = (row[3])
        Region = row[4]
        Continent = row[5]
        Location = row[6]
        OFDA_Response = row[7]
        Appeal = row[8]
        Declaration = row[9]
        Local_Time = row[10]
        Start_Year = row[11]
        Start_Month = row[12]
        Start_Day = row[13]
        End_Year = row[14]
        End_Month = row[15]
        End_Day = row[16]
        Total_Deaths = row[17]
        insured_damages_usd = row[18]
        Total_Damages_usd = row[19]
        CPI = row[20]

        cur.execute('INSERT INTO details VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Dis_ID, Seq, Disaster_Subgroup, Disaster_Subtype,
                                                                                            Region, Continent, Location,OFDA_Response,Appeal,Declaration,
                                                                                            Local_Time,Start_Year,Start_Month,Start_Day,End_Year,End_Month,End_Day,
                                                                                            Total_Deaths,insured_damages_usd,Total_Damages_usd,CPI))
        conn.commit()
    print("data parsed successfully");

    conn.close()