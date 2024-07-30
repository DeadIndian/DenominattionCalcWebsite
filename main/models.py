from django.db import models

# Create your models here.
class Calculator(models.Model):
	name = models.IntegerField(unique=True)

	def __str__(self):
		return str(self.name)