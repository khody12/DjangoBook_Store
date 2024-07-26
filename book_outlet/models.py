from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model): #models.Model is supplied by django to us. 
    title = models.CharField(max_length=50)  # you get the value types from the models module. # charfield is used for small to large-sized strings. have to set 
    #Not for something that is multiple book pages
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) # integer numbers. 
    author = models.CharField(null=True, max_length=100) # these two new fields, author and is_bestselling were added after we make initial migrations, this means we have to set default values for them,
    is_bestselling = models.BooleanField(default=False) # the sql datatable doesnt allow for empty values, (null is okay even though not optimal) 
    #we have to have some default if were adding on new attributes after making migrations. or we could say blank=True and allow blank values.
    slug = models.SlugField(default="",null=False) # this will slugify whatever is passed in. 

    def get_absolute_url(self):
        return reverse("book", args=[self.id])

    def __str__(self): # overriding this function as it basically exists for every python class. it allows us to change how something can be output in the terminal.
        return f"{self.title} ({self.rating})"
    def save(self, *args, **kwargs): #*args and **kwargs is used when we dont know how many arguments are going to be passed in. *args handles all positional arguments and will put the arguments in a tuple.
        #**kwargs will handle all keywords, so things like title="sometitle", name="somename". these arguments will be put into a dictionary. this is important for something like overriding the save function
        #because we may have more arguments to save in the future if we update our model.
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)



