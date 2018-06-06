# DGjango p133

from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField()
	email = forms.EmailField(required=False)
	message = forms.CharField()

# f2 = ContactForm({'subject': 'Hello', 'e-mail': 'adrian@example.com', 'message': 'Nice site!'})