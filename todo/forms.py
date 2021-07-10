from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import works
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user
class DateInput(forms.DateInput):
	input_type="date"
class AdditemForm(forms.ModelForm):
	class Meta:
		model=works
		fields=['work','Description','DeadLine',]
		widgets={
		'DeadLine':DateInput(),
		}
