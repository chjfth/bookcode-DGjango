# -*- coding: utf-8 -*-
import time

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
	return response

