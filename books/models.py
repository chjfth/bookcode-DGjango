# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True, verbose_name='e-mail')

	def __str__(self):
		return "%s %s"%(self.first_name, self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author) # many-to-many
	publisher = models.ForeignKey(Publisher) # many-to-one
	publication_date = models.DateField()

#end0
