# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=60, blank=True)
	state_province = models.CharField(max_length=30, blank=True)
	country = models.CharField(max_length=50)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True, verbose_name='e-mail')

	def __str__(self):
		return "%s %s"%(self.first_name, self.last_name)

#
# p197 new: 
#
class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author) # many-to-many
	publisher = models.ForeignKey(Publisher) # many-to-one
	publication_date = models.DateField()

	def __str__(self):
		return self.title

	objects = BookManager() # p197 new, 'class BookManager' must has have been defined



