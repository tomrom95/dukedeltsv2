from django import forms
from localflavor.us.forms import USPhoneNumberField
from django.forms.extras.widgets import SelectDateWidget

class AlumniForm(forms.Form):
	email = forms.EmailField(required=True)
	name = forms.CharField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea)
	
class RushForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	phone_number = USPhoneNumberField()
	year = forms.ChoiceField(choices=(('2019', '2019',), ('2018', '2018',)))
