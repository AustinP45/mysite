from django.db import models

from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name
	
class Assignment(models.Model):
	course = models.ForeignKey(Course)
	task = models.CharField(max_length=80)
	desc = models.CharField(max_length=200)
	dueDate = models.DateField('Due date')
	estHrsToComplete = models.DecimalField(max_digits=5, decimal_places=2)
	actHrsToComplete = models.DecimalField(max_digits=5, decimal_places=2)
	complete = models.BooleanField(default=False)
	
	def __str__(self):
		return self.task

