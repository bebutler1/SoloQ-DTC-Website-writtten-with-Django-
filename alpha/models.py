from django.db import models

# Create your models here.
class DataForm(models.Model):
    your_name = models.CharField(max_length=30)
    champion = models.CharField(max_length=30, default = '')
    role = models.CharField(max_length=7)
    teammate_1 = models.CharField(max_length=30)
    teammate_2= models.CharField(max_length=30)
    teammate_3 = models.CharField(max_length=30)
    teammate_4 = models.CharField(max_length=30)
    outcome = models.CharField(max_length=4)
    mute = models.CharField(max_length=3)
    attitude_Score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return 'Player was: ' + self.your_name + ' | ' + self.role + ' | ' + self.outcome
    


    
    
