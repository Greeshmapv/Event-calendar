from django.db import models

class Payment(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Event(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    payment_details = models.ForeignKey(Payment, on_delete=models.CASCADE)
    contact_phone = models.CharField(max_length=20)


class Details(models.Model):
    name= models.CharField(max_length=255)
    img=models.ImageField(upload_to="pic")
    description=models.CharField(max_length=255)




    def __str__(self):
        return self.name
