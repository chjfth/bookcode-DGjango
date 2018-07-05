# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render


def ch13getpng(request):
	image_data = open("flower.png", "rb").read()
	return HttpResponse(image_data, content_type="image/png")
