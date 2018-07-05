# -*- coding: utf-8 -*-
import time
import csv # CH13 use 

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render


def ch13getpng(request):
	image_data = open("flower.png", "rb").read()
	return HttpResponse(image_data, content_type="image/png")


# https://docs.djangoproject.com/en/1.11/ref/request-response/#httpresponse-objects
def ch13_write_twice(request):
	response = HttpResponse("<p>My line 0") # this will appear as response[0]
	
	response.write("<p>Here's the text of the Web page.</p>") # appear as response[1]
	
	time.sleep(1.0) # note: this does not produce HTTP chunked data, which  requires StreamingHttpResponse

	# response.content = "<p>Start-again" # this will start from(=overwrite) response[0]

	response['aGe'] = 120
	response.write("<p>Here's another paragraph.</p>")
	return response

# CH13: unruly_passengers_csv

# Number of unruly passengers each year 1995 - 2007. In a real application
# this would likely come from a database or some other back-end data store.
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273, 281,304,203, 134, 147]

def unruly_passengers_csv(request):
	
	# Create the HttpResponse object with the appropriate CSV header.
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=unruly.csv'

	# Create the CSV writer using the HttpResponse as the "file."
	writer = csv.writer(response)
	writer.writerow(['Year', 'Unruly Airline Passengers'])

	for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
		writer.writerow([year, num])
	
	return response


