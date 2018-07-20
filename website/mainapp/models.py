from django.db import models

class Main(models.Model):
	
	def __str__(self):
		return self.name

	def __init__(self, arg):
		super(Main, models.Model).__init__()
		self.arg = arg
		
