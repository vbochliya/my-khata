from django.db import models

class khata_transactions(models.Model):
    datetime=models.DateField()
    name=models.CharField(max_length=100)
    ammount=models.CharField(max_length=20)
    catagory=models.CharField(max_length=20)


    def __str__(self):
        return self.name



class given_taken(models.Model):
    datetime=models.DateField()
    name=models.CharField(max_length=100)
    ammount=models.CharField(max_length=20)
    catagory=models.CharField(max_length=20)


    def __str__(self):
        return self.name