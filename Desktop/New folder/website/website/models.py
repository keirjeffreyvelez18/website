from django.db import models
from datetime import time

class Program(models.Model):
	program_name = models.CharField(null="", max_length=100)
	program_description = models.CharField(null="", max_length=2000)
	program_department = models.CharField(null="", max_length=50)
	program_level = models.CharField(null="", max_length=1000)

	def __str__(self):
		return self.program_name

class UpcomingEvent(models.Model):
	title = models.CharField(null="",max_length=1000)
	contents = models.CharField(null="",max_length=10000)
	date = models.DateField(null="")
	time = models.TimeField(null="", help_text="Format: HH:MM:SS, 24H. e.g 15:30:00 is 3:30PM")
	event_datecreated = models.DateTimeField(null="",auto_now_add=True)
	image = models.FileField(null=True)

	def __str__(self):
		return self.title

class ResearchTitle(models.Model):
	research_title = models.CharField(null="", max_length=1000)
	research_abstract = models.TextField(null="", max_length=50000)
	research_author = models.CharField(null="", max_length=1000)
	research_resources = models.CharField(null="", max_length=10000)
	# research_program = models.CharField(null="", max_length=1000)
	# research_year = models.PositiveIntegerField( default=0)

	def __str__(self):
		return self.research_title+" by "+self.research_author

class FacultyMember(models.Model):
	faculty_Last_Name = models.CharField(null="", max_length=100)
	faculty_First_Name = models.CharField(null="", max_length=100)
	faculty_Middle_Name = models.CharField(null="", max_length=100)
	First_Semester = models.BooleanField(default=True)
	Second_Semester = models.BooleanField(default=True)

	def __str__(self):
		return self.faculty_Last_Name+", "+self.faculty_First_Name

class OutreachPost(models.Model):
	title = models.CharField(null="", max_length=50)
	author = models.CharField(null="", max_length=50)
	date = models.DateField(null="", auto_now_add=True)
	contents = models.CharField(null="", max_length=5000)
	image = models.FileField()

	class Meta:
		get_latest_by = 'date'

	def __str__(self):
		return self.title+" by "+self.author

class NewsPost(models.Model):
	title = models.CharField(null="", max_length=1000, help_text="Headline")
	contents = models.CharField(null="",max_length=10000, help_text="Full content")
	author = models.CharField(null="",max_length=1000, help_text="Author of the article")
	image = models.FileField(null=True, help_text="Headline Image of the article")
	date = models.DateField(null="")
	time = models.TimeField(null="", auto_now_add=True)

	def __str__(self):
		return  self.title

class Alumni(models.Model):
	alumni_name = models.CharField(null="", max_length=1000, help_text="Full name along with prefix and suffixes.")
	alumni_description = models.CharField(null="", max_length=5000, help_text="Short Bio of the alumni")
	alumni_contact = models.CharField(null="", max_length=5000, help_text="LinkedIn URL, Contact Number")
	alumni_image = models.FileField(null="", help_text="2x2 or Professional Image of the Alumni")
	alumni_url = models.URLField(null="", help_text="LinkedIn / Professional Website of the Alumni")

	def __str__(self):
		return self.alumni_name


# to migrate database use the following commands
# python manage.py makemigrations [nameofApp]
# python manage.py sqlmigrate [nameofApp] ###
# python manage.py migrate
