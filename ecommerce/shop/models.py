from django.db import models
#from datetime import DateTimeField



class Catalog(models.Model):
    name = models.CharField(max_length=255)
    #slug = models.SlugField(null=True)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    #pub_date = models.DateTimeField(default=datetime.now)
    #def __str__(self):
        #return self.name + ' - ' + self.publisher



class Product(models.Model):
    catalog=models.ForeignKey(Catalog,on_delete=models.CASCADE)
    # = models.SlugField(max_length=150)
    name=models.CharField(max_length=200)
    description = models.TextField()
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_rupees = models.DecimalField(max_digits=6,decimal_places=2)
