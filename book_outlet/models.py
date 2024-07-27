from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Book(models.Model): #models.Model is supplied by django to us. 
    title = models.CharField(max_length=50)  # you get the value types from the models module. # charfield is used for small to large-sized strings. have to set 
    #Not for something that is multiple book pages
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) # integer numbers. 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # ForeignKey() tells us that author is a pointer at an entry within the Author Model. 
    #^^^^on_delete parameter necessary because if an author is deleted, we need to know what happens to the book that is related to the author
    #cascade would affect all related models. protect would avoid deleting related models.

    is_bestselling = models.BooleanField(default=False) # the sql datatable doesnt allow for empty values, (null is okay even though not optimal) 
    #we have to have some default if were adding on new attributes after making migrations. or we could say blank=True and allow blank values.
    slug = models.SlugField(default="",null=False, db_index=True) # this will slugify whatever is passed in. 
    
    #we can improve the performance of the find operation by making an index for some of our attributes. db_index = database index. Use this for attributes that you will very often need to fetch.

    def get_absolute_url(self):
        return reverse("book", args=[self.id])

    def __str__(self): # overriding this function as it basically exists for every python class. it allows us to change how something can be output in the terminal.
        return f"{self.title} ({self.rating})"
    def save(self, *args, **kwargs): #*args and **kwargs is used when we dont know how many arguments are going to be passed in. *args handles all positional arguments and will put the arguments in a tuple.
        #**kwargs will handle all keywords, so things like title="sometitle", name="somename". these arguments will be put into a dictionary. this is important for something like overriding the save function
        #because we may have more arguments to save in the future if we update our model.
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)





