# a script to read in all the csv files in a folder
# then upload them to the given database using ogr2ogr

from osgeo import ogr
from subprocess import call
import csv
import os
from os import path
from os import listdir
import fileinput
import string

#CHANGE THESE

#path to the folder
dir_path = os.path.dirname(os.path.realpath(__file__))
#if csvs are in sub folder point to that
dir_name =  dir_path + "/csv/upload"

host  = ""
user = ""
db = ""
password = ""



#function that finds all csv files in the given filename and  returns it
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

# get array of file names that end in .csv in the selected directory
filenames = find_csv_filenames(dir_name)


def ogr2ogr_to_Db(filename):

    db_name = filename.split("/")[-1]
    db_name = db_name.split(".")[0]
    print db_name

    call(['ogr2ogr','-f',
        'PostgreSQL','PG:host=' + host + ' user=' + user + ' dbname=' + db + ' password='+password+'',
        filename,
        "-nln",
        db_name
        ])

    print db_name + " added to the database"


for name in filenames:
    # call function to open csv file and read in rows
    full_path_csv = dir_name +"/"+ name
    #call function to upload to db
    ogr2ogr_to_Db(full_path_csv)


print "Done running ogr_to_db!"
