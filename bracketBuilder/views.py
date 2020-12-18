from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import models
from . import forms

# Create your views here.
def index(request):
    brackets = models.BracketModel.objects.all()
    title = "Bracket Builder"
    content = "Content"
    context = {
        "title":title,
        "body":content, 
        "authenticated":False, #can use {{% if authenticated %}} {{%end if%}} to hide stuff
        "brackets":brackets,
    }
    return render(request, "index.html", context=context)

#form submission seems to be broken
@login_required #this redirects them to login page, then right back to where they were once they do
def createBracket(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            bracket_form = forms.BracketForm(request.POST)
            if bracket_form.is_valid():
                bracket_form.save(request)
                bracket_form = forms.BracketForm()
            else:
                messages.error(request, "Form is not valid")
        else:
            messages.error(request, "User is not logged in")
    else:
        bracket_form = forms.BracketForm()
        messages.error(request, "Method is not POST")
    title = "Create a bracket"
    context = {
        "title":title,
        "form":bracket_form,
    }
    return render(request, "createBracket.html", context=context)

def get_brackets(request):
    bracket_object = models.BracketModel.objects.all()
    bracket_list = {}
    bracket_list["brackets"] = []
    for brack in bracket_object:
        temp_bracket = {}
        temp_bracket["bracket_name"]=brack.bracket_name
        temp_bracket["host"]=brack.host.username
        temp_bracket["primary_contact_type"]=brack.primary_contact_type
        temp_bracket["primary_contact_value"]=brack.primary_contact_value
        temp_bracket["start_date"]=brack.start_date
        temp_bracket["end_date"]=brack.end_date
        temp_bracket["tournament_description"]=brack.tournament_description
        temp_bracket["location"]=brack.location
        temp_bracket["id"]=brack.id 
    bracket_list["brackets"]+=[temp_bracket]
    return JsonResponse(bracket_list)

def postedTournament(request, page=1, room_name='1'):
    bracket = models.BracketModel.objects.get(id=page)
    title = bracket.bracket_name
    content = "Content"
    context = {
        "title":title,
        "body":content, 
        "bracket":bracket,
        "room_name":room_name
    }
    return render(request, "chat/postedTournament.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance
    }
    return render(request, "registration/register.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/")
#lecture 5 at the 1 hour mark goes over how to do a
#next and previous to jump between pages