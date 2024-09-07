from django.db import models

# Create your models here.
class InUseCars(models.Model):
    ceoNumber = models.IntegerField()
    carNumber = models.IntegerField()


class RegistredCars(models.Model):
    carNumber = models.IntegerField()


class EmployesInfo(models.Model):
    ceoNumber = models.IntegerField()
    ceoName = models.CharField(max_length=100)
    phoneNumber = models.IntegerField( default='0000000000')
    email = models.EmailField(default='example@example.com')

    
    def __str__(self):
        return str(f" name: {self.ceoNumber}   ceo number: {self.ceoName} ")

