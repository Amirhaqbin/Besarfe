from django.db import models


class Customer(models.Model):

    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

