from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'groups'  # Указываем имя существующей таблицы

    def __str__(self):
        return self.name