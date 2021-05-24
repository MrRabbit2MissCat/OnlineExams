from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True, max_length=150)
    department = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'user'
