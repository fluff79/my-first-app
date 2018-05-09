from django.db import models
from django.utils import timezone
import datetime

class Item(models.Model):

	FREEZER_DRAWERS = (
			(1, 'Kitchen: Top tray'),
			(2, 'Kitchen: Middle drawer'),
			(3, 'Kitchen: Bottom drawer'),
			(4, 'Utility: Top tray'),
			(5, 'Utility: 1st drawer'),
			(6, 'Utility: 2nd drawer'),
			(7, 'Utility: 3rd drawer'),
			(8, 'Utility: 4th drawer'),
			(9, 'Utility: 5th drawer'),
			)
			
	TYPES = (
			(1, 'Raw meat'),
			(2, 'Fruit and veg'),
			(3, 'Meal'),
			(4, 'Dessert'),
			(5, 'Other'),
			)

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField("food", max_length=100)
	text = models.TextField()
	item_type = models.IntegerField(choices = TYPES, default = 1)
	added_date = models.DateField("date added", default=datetime.date.today)
	where = models.IntegerField(choices = FREEZER_DRAWERS, default = 1)
	expires_date = models.DateField(default = datetime.date.today)

	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# Create your models here.
