# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from books.models import Book

# Create your views here.

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		return render_to_response('search_results.html', {'books': books, 'query': q})
	else:
		message = 'Please submit a search term.'
	return HttpResponse(message)
