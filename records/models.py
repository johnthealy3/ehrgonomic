from django.db import models

class Record(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name 

# Create your models here.
