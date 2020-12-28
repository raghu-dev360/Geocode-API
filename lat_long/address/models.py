from django.db import models

# Create your models here.


class AddressFile(models.Model):
    file = models.FileField(upload_to='add_file/')
