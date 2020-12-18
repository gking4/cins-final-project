from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BracketModel(models.Model):
        #probably have to add a host name field, then load it in from username when form is submitted?
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    bracket_name = models.CharField(max_length=500, default="Bracket Name")
    primary_contact_type = models.CharField(max_length=500,default="Email")
    primary_contact_value = models.CharField(max_length=500, default="Jenna", blank=True)
    start_date = models.DateField() #change to date-time
    end_date = models.DateField() #change to date-time
    tournament_description = models.CharField(max_length=30000, default="A new tournament.")
    location = models.CharField(max_length=500, default="Online")

    def __str__(self):
        return self.bracket_name

    def gethost(self):
            return self.host

    def getContactType(self):
            return self.primary_contact_type
    
    def getContact(self):
            return self.primary_contact_value

    def getStartDate(self):
            return self.start_date

    def getEndDate(self):
            return self.end_date

    def getDescription(self):
            return self.tournament_description

    def getLocation(self):
            return self.location

    def getBracketName(self):
            return self.bracket_name

    def getID(self):
         return self.id  