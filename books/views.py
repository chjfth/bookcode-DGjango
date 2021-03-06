# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.mail import send_mail

from books.models import Book

# Create your views here.

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term')
		elif len(q)>20:
			errors.append('Please enter at most 20 characters')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books': books, 'query': q})

	return render(request, 'search_form.html', {'errors':errors})


######### DGjango p136 ##########

from .forms import ContactForm

#from django.views.decorators.csrf import csrf_protect

def contact0(request):
	return contact(request, 0)

def contact1(request):
	return contact(request, 1)

def contact(request, mystyle):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
#			send_mail(
#				cd['subject'],
#				cd['message'],
#				cd.get('email', 'noreply@example.com'),
#				['siteowner@example.com'],
#			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'your initial value!'}
			)
	
	form_html = 'contact_form.html' if mystyle==0 else 'contact_form_u1.html'
	
	return render(request, form_html, {'form': form })


def contact_thanks(request):
	return HttpResponse('Thank you for contacting~')
