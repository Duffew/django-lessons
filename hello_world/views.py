from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Adjust the view so that if the request method is POST, a HttpResponse is returned, 
    # that says, "You must have POSTed something".
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    # Otherwise, return an HttpResponse so that, instead of plain text, 
    # we return the method of the request object.
    else:
        return HttpResponse(request.method)
        
