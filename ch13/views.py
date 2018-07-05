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

	response.write("<p>Here's another paragraph.</p>")

	response['aGe'] = 120 # just a test, ok, client side sees this HTTP header
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

# CH13: Generate PDF

from reportlab.pdfgen import canvas

def hello_pdf(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'

	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, "Hello world.")

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response


# CH13: Using BytesIO for improved performance
#
from io import BytesIO

def hello_pdf2(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello2.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world with BytesIO.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response 

