from django.db import models

class User(models.Model):
    name = models.CharField("name", max_length=50)
    birth = models.DateField("birth", auto_now=False, auto_now_add=False)
    cep = models.CharField("cep", max_length=8)
    street = models.CharField("street", max_length=100)
    home_number = models.CharField("home_number", max_length=10)
    neighborhood = models.CharField("neighborhood", max_length=50)
    city = models.CharField("city", max_length=100)
    country = models.CharField("country", max_length=100)
    phone = models.CharField("phone_number", max_length=50)
    email = models.EmailField("email", max_length=254)

