from django.db import models

# Create your models here.
class Family(models.Model):

    name = models.CharField(max_length=60)
    birth = models.DateField()
    document = models.IntegerField(primary_key=True)

