from django.db import models

# Create your models here.

class Book(models.Model): #models.Model is supplied by django to us. 
    title = models.CharField(max_length=50)  # you get the value types from the models module. # charfield is used for small to large-sized strings. have to set 
    #Not for something that is multiple book pages
    rating = models.IntegerField() # integer numbers. 

    def __str__(self): # overriding this function as it basically exists for every python class. it allows us to change how something can be output in the terminal.
        return f"{self.title} ({self.rating})"



