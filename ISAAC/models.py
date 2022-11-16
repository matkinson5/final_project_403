from django.db import models

# Create your models here.

class resources(models.Model):
    class_title = models.CharField(max_length = 5)
    resource_name = models.CharField(max_length = 50)
    link = models.CharField(max_length = 255)

    def __str__(self):
        return(self.resource_name)
    class Meta:
        db_table = 'resources'


