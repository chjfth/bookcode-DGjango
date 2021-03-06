""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
#from django.views.generic import TemplateView

from views import hello, current_datetime, hours_ahead
from books import views

import ch13.views as ch13v

from django.conf.urls import handler404
#handler404 = current_datetime # a test, ok

urlpatterns = [
	url(r'^$', hello),
	
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	
#	url(r'^search-form/$', views.search_form), # no need now
	url(r'^search/$', views.search),

	url(r'^contact/$', views.contact0),
	url(r'^contact1/$', views.contact1),
	url(r'^contact/thanks/$', views.contact_thanks),

	url(r'^ch13getpng$', ch13v.ch13getpng),
	url(r'^ch13wt$', ch13v.ch13_write_twice),
	url(r'^ch13csv$', ch13v.unruly_passengers_csv),
	url(r'^ch13pdf$', ch13v.hello_pdf),
	url(r'^ch13pdf2$', ch13v.hello_pdf2),
	
	url(r'^admin/', admin.site.urls),
#	url(r'^about/', about_views.contact),
]
