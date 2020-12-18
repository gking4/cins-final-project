from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from . import models

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email is already in use.")
    return value


#dont use model forms except for the one example in lecture
#see lecture 7 at 1 hour mark for more info on validation

class BracketForm(forms.Form):
    bracket_name = forms.CharField(
        label='Bracket Name',
        required=True,
        max_length=500,
    )
    primary_contact_type = forms.ChoiceField(
        choices= (
            ("Email", "Email"),
            ("Website Chat", "Chat"),
            ("Discord", "Discord"),
        ),
        required=True,
    )
    primary_contact_value = forms.CharField(
        label='Primary Contact',
        required=False,
        max_length=500,
    )
    start_date = forms.DateField()
    end_date = forms.DateField()
    tournament_description = forms.CharField(
        label="Description",
        required=True,
        max_length=30000,
    )
    location = forms.CharField(
        label="Location",
        required=True,
        max_length=500,
    )

    def save(self, request):
        #potentially save an extra value of cleaned bracketname so it can be used as a url?
        #note: probably put in more cleaning stuff later and possibly some if stuff about value that doesnt need to be true?
        bracket_instance = models.BracketModel()
        bracket_instance.bracket_name = self.cleaned_data["bracket_name"]
        bracket_instance.host = request.user
        bracket_instance.primary_contact_type = self.cleaned_data["primary_contact_type"]
        bracket_instance.primary_contact_value = self.cleaned_data["primary_contact_value"]
        bracket_instance.start_date = self.cleaned_data["start_date"]
        bracket_instance.end_date = self.cleaned_data["end_date"]
        bracket_instance.tournament_description = self.cleaned_data["tournament_description"]
        bracket_instance.location = self.cleaned_data["location"]
        bracket_instance.save()
        return bracket_instance

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = User
        fields = ("username", "email",
                    "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
