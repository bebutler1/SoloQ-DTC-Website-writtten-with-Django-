from django.db import models

# Create your models here. Database stuff


class Post(models.Model): #creates a table called posts
    title = models.CharField(max_length=140) #Syntax: name = datatype(constraints)
    body = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return self.title #returns a list of titles 
    
