'''
this code used for a csv to sqlite database import
'''

#from django.db import models

from app.models import car as carO

import csv

dataReader = csv.reader(open('app/Vehicles.csv'), delimiter=',', quotechar='"')

#delete old data
carO.objects.all().delete()

#insert new data
#skip 1stHEADERrow
next(dataReader)
for row in dataReader:
    car=carO()
    car.Vehicle_ID=row[0]
    car.Make=row[1]
    car.Short_Model=row[2]
    car.Long_Model=row[3]
    car.Trim=row[4]
    car.Derivative=row[5]
    car.Year_introduced=row[6]
    car.Year_discontinued=row[7]
    car.Currentl_Available=row[8]
    car.save()
