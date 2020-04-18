from django.db import models
from django.contrib.auth.models import User

# models for menu items.

class RegularPizza(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="regular", null=True)
    firstTop = models.CharField(max_length=64, default = "None")
    secondTop = models.CharField(max_length=64, default = "None")
    thirdTop = models.CharField(max_length=64, default = "None")
    size = models.CharField(max_length=64, default='Small')
    price = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    def __str__(self):
        if self.firstTop == "Cheese":
            return f"Regular Pizza: Cheese - {self.firstTop} - {self.size} - {self.price} \n"
        if self.firstTop == "Special":
            return f"Regular Pizza: Special - {self.firstTop} - {self.size} - {self.price} \n"
        return f"Regular pizza: {self.firstTop} - {self.secondTop} - {self.thirdTop} - {self.size} - {self.price} \n"
    class Meta:
      db_table = "regularpizza"

class SicilianPizza(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sicily", null=True)
    firstTop = models.CharField(max_length=64, default = "None")
    secondTop = models.CharField(max_length=64, default = "None")
    thirdTop = models.CharField(max_length=64, default = "None")
    size = models.CharField(max_length=64, default='Small')
    price = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    def __str__(self):
        if self.firstTop == "Cheese":
            return f"Regular Pizza: Cheese - {self.firstTop} - {self.size} - {self.price} \n"
        if self.firstTop == "Special":
            return f"Regular Pizza: Special - {self.firstTop} - {self.size} - {self.price} \n"
        return f"Sicilian pizza: {self.firstTop} - {self.secondTop} - {self.thirdTop} - {self.size} - {self.price} \n"
    class Meta:
      db_table = "sicilianpizza"

class Subs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subway", null=True)
    flavor = models.CharField(max_length=64, default = "None")
    size = models.CharField(max_length=64, default='Small')
    mushroom = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    onion = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    pepper = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    cheese = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    def __str__(self):
        return f" Sandwich: {self.flavor} - {self.size} - Mushroom: {self.mushroom} - Onion: {self.onion} - Pepper: {self.pepper} - Cheese: {self.cheese} - Price: {self.price} \n"
    class Meta:
      db_table = "sub"

class Pasta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="macaroni", null=True)
    flavor = models.CharField(max_length=64, default = "None")
    price = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    size = models.CharField(max_length=64, default="Regular")
    def __str__(self):
        if self.size != "Regular":
            return f"Platter: {self.flavor}-{self.size}-{self.price} \n"
        return f"Pasta: {self.flavor} - {self.price} \n"
    class Meta:
      db_table = "pasta"

class Salads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="greens", null=True)
    flavor = models.CharField(max_length=64, default = "None")
    price = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    size = models.CharField(max_length=64, default="Regular")
    def __str__(self):
        if self.size != "Regular":
            return f"Platter: {self.flavor}-{self.size}-{self.price} \n"
        return f"Salads: {self.flavor} - {self.price} \n"
    class Meta:
      db_table = "salads"

class Parm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parmesan", null=True)
    flavor = models.CharField(max_length=64, default = "None")
    price = models.DecimalField(max_digits=10, default = 0, decimal_places=2, null=True)
    size = models.CharField(max_length=64, default="Regular")
    def __str__(self):
        if self.size != "Regular":
            return f"Platter: {self.flavor}-{self.size}-{self.price} \n"
        return f"Parm: {self.flavor} - {self.price} \n"
    class Meta:
      db_table = "parm"
