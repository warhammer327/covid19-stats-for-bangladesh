from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Home(models.Model):

	date = models.DateTimeField()
	confirmedin_dhaka = models.IntegerField(null=True)
	confirmedin_rajshahi = models.IntegerField(null=True)
	confirmedin_khulna = models.IntegerField(null=True)
	confirmedin_sylhet = models.IntegerField(null=True)
	confirmedin_chattogram = models.IntegerField(null=True)
	confirmedin_barishal = models.IntegerField(null=True)
	confirmedin_rangpur = models.IntegerField(null=True)
	confirmedin_mymensingh = models.IntegerField(null=True)

	def __str__(self):
		return self.date + 'home'
