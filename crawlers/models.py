from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	def __str__(self):
		return self.name

class Solution(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	def __str__(self):
		return self.name

class Service(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	def __str__(self):
		return self.name

class Log(models.Model):
	description = models.CharField(max_length=150)
	success = models.BooleanField()
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description

class CrawlerInstruction(models.Model):
	KIND_CHOICES = (
		('PR', 'Product'),
		('SL', 'Solution'),
		('SE', 'Service'),
	)
	instrunction = models.TextField(max_length=150)
	url = models.URLField(max_length=200)
	kind = models.CharField(max_length=50, choices=KIND_CHOICES)
	
	def __str__(self):
		return self.kind

