from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""topic of notes"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User) # attach each topic to a specific user

	def __str__(self):
		"""return text string"""
		return self.text

class Entry(models.Model):
	"""specific knowledge of this topic"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."