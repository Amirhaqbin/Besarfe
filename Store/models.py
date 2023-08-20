from django.db import models

class product(models.Model):
    name = models.CharField(max_length=123)
    expire_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    

class Specialoffer(models.Model):
    store = models.ForeignKey('store', on_delete=models.CASCADE)
    offer_product = models.ManyToManyField(product, related_name= 'specialsoffers')

    def __str__(self):
        return f"Special Offer from {self.store}"
    

class store(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

    

