from django.shortcuts import render

# Give the about app similar functionality to the hello_world app, 
# except it should return a HttpResponse of "This would be the about page" instead.
from django.http import HttpResponse

# Create your views here.
# The view name should be about_me.
def about_me(request):
    return HttpResponse("This would be the about page")
