# DGjango p133

from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=20)
	email = forms.EmailField(required=False, label='Your E-mail')
	message = forms.CharField(widget=forms.Textarea)
	
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words<4:
			raise forms.ValidationError('Not enough words, need 4!')
		return message # + u'@Q' // yes can interpolate the cleaned result
	

# f2 = ContactForm({'subject': 'Hello', 'e-mail': 'adrian@example.com', 'message': 'Nice site!'})