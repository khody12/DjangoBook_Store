from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model): #THIS WILL BE A ONE TO ONE RELATION.
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta: # this meta class changes how things are output within the admin page. 
        verbose_name_plural = "Address Entries"
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)   # ForeignKey() is used for a one-to-many relation, while OneToOneField is obviously one to one.
    #null=True will allow us to make the migrations. we will initially get an error because we don't have a default value and we have existing data that doesnt have an address tied to author.
    #null=True is basically allowing this field to be set to null. 

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

class Book(models.Model): #models.Model is supplied by django to us. 
    title = models.CharField(max_length=50)  # you get the value types from the models module. # charfield is used for small to large-sized strings. have to set 
    #Not for something that is multiple book pages
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) # integer numbers. 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,related_name="books") # ForeignKey() tells us that author is a pointer at an entry within the Author Model. ONE-TO-MANY RELATION <------------ 
    #^^^^on_delete parameter necessary because if an author is deleted, we need to know what happens to the book that is related to the author
    #cascade would affect all related models. protect would avoid deleting related models.

    is_bestselling = models.BooleanField(default=False) # the sql datatable doesnt allow for empty values, (null is okay even though not optimal) 
    #we have to have some default if were adding on new attributes after making migrations. or we could say blank=True and allow blank values.
    slug = models.SlugField(default="",null=False, db_index=True) # this will slugify whatever is passed in. 

    published_countries = models.ManyToManyField(Country)
    
    #we can improve the performance of the find operation by making an index for some of our attributes. db_index = database index. Use this for attributes that you will very often need to fetch.

    def get_absolute_url(self):
        return reverse("book", args=[self.id])

    def __str__(self): # overriding this function as it basically exists for every python class. it allows us to change how something can be output in the terminal.
        return f"{self.title} ({self.rating})"





