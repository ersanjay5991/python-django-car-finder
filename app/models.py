from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    #user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    sample_image = models.ImageField(upload_to='profile_image', blank=True)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
#post_save.connect(create_profile, sender=User)


class car(models.Model):  
				Vehicle_ID = models.CharField(max_length=20)  
				Make = models.CharField(max_length=40)
				#Images_path = models.CharField(max_length=40)  
				Short_Model = models.CharField(max_length=35)  
				Long_Model = models.CharField(max_length=50)
				Trim = models.CharField(max_length=35) 
				Derivative = models.CharField(max_length=35) 
				Year_introduced = models.CharField(max_length=5) 
				Year_discontinued = models.CharField(max_length=5) 
				Curbookvehiclel_Available = models.CharField(max_length=10)
				model_pic = models.ImageField(upload_to = 'media', default='default.jpeg')
				
				class Meta:  
								db_table = "car"  

				def __str__(self):
					return self.Vehicle_ID

class bookvehicle(models.Model):
				Vehicle_ID = models.CharField(max_length=20)
				used_email = models.CharField(max_length=20)
				start_date = models.CharField(max_length=20)
				end_date = models.CharField(max_length=20)
				
				class Meta:
								db_table = "bookvehicle" 


class contact(models.Model):
				name = models.CharField(max_length=30)
				mono= models.CharField(max_length=13)
				email = models.CharField(max_length=30)
				msg = models.CharField(max_length=50)
				
				
				class Meta:
								db_table = "contact" 


'''import csv

dataReader = csv.reader(open("./Vehicles.csv"), delimiter=',', quotechar='"')

for row in dataReader:
				car=car()
				car.Vehicle_ID=row[1]
				car.Make=row[2]
				car.Short_Model=row[3]
				car.Long_Model=row[4]
				car.Trim=row[5]
				car.Derivative=row[6]
				car.Year_introduced=row[7]
				car.Year_discontinued=row[8]
				car.Curbookvehiclel_Available=row[9]
				car.save()
'''