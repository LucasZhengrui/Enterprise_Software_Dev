import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
import sqlite3
from disaster_table.models import summary,details

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        summary.objects.all().delete()
        print("table dropped successfully")

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/disaster_table/nartural_disasters_information/disasters_summary.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                # print(row)

                summary_object = summary.objects.create(
                    Dis_ID=int(row[0]),
                    Year = int(row[1]),
                    Disaster_Group = row[2],
                    Disaster_Type = row[3],
                    Country = row[4],
                    ISO = row[5],
                    Total_Affected = row[6],
                    Total_Damages = row[7],
                )
                summary_object.save()
         # drop the data from the table so that if we rerun the file, we don't repeat values
        details.objects.all().delete()
        print("table dropped successfully")

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/disaster_table/nartural_disasters_information/disasters_details.csv',
                  newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                print(row)

                details_object = details.objects.create(
                    Dis_ID=summary.objects.get(Dis_ID=int(row[0])),
                    Seq = int(row[1]),
                    Disaster_Subgroup = row[2],
                    Disaster_Subtype = row[3],
                    Disaster_Subsubtype = row[4],
                    Region = row[5],
                    Continent = row[6],
                    Location = row[7],
                    OFDA_Response = row[8],
                    Appeal = row[9],
                    Declaration = row[10],
                    Local_Time = row[11],
                    Start_Year = row[12],
                    Start_Month = row[13],
                    Start_Day = row[14],
                    End_Year = row[15],
                    End_Month = row[16],
                    End_Day = row[17],
                    Total_Deaths = row[18],
                    insured_damages_usd = row[19],
                    Total_Damages_usd = row[20],
                    CPI = row[21],
                )
                details_object.save()
        print("data parsed successfully")
        
        
         # Initialization disaster_message and disaster_user data
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS disaster_message;")
        cursor.execute("CREATE TABLE disaster_message (id INTEGER NOT NULL, message TEXT NOT NULL, PRIMARY KEY (id));")
        cursor.execute("INSERT INTO disaster_message VALUES (1, 'Welcome to the management system, if you have any questions please contact l.wang.22@abdn.ac.uk, r.zheng.22@abdn.ac.uk，t05bl22@abdn.ac.uk，t16cl22@abdn.ac.uk');")
        cursor.execute("DROP TABLE IF EXISTS disaster_user;")
        cursor.execute("CREATE TABLE disaster_user (user_id INTEGER, user_password TEXT, user_name TEXT, user_level INTEGER, login_status TEXT, is_banned INTEGER, is_delete INTEGER, is_approved INTEGER, PRIMARY KEY (user_id));")
        cursor.execute("INSERT INTO disaster_user VALUES (1, '21232f297a57a5a743894a0e4a801fc3', 'admin', 3, '1', 0, 0, 1);")
        connection.commit()

        print("Initialization data successfully")