# Generated by Django 4.2.14 on 2024-07-25 02:43
#this was generated when we did python3 manage.py makemigrations, this simply creates the operations, but they havent been performed yet.
#these are the operations django should perform against the database. 
# Migration is basically a class 
# python3 manage.py migrate will actually apply these operations against the database. 


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True # meaning this is the first migration performed. 

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
