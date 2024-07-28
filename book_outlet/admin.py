from django.contrib import admin
from .models import Book, Author, Address, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("title",)} # both slug and title is a field name here. 
    list_filter = ("author","rating",)
    list_display = ("title", "author",)
    #django knows what to do here because it understands that slug is a slug field, and it'll make a slug based off the tuple that is passed in.





admin.site.register(Book,BookAdmin)
admin.site.register(Author,)
admin.site.register(Address,)
admin.site.register(Country,)



