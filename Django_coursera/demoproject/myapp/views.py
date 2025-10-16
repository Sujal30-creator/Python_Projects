from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menuitems(request,dish):
    items={
        'pasta':'pasta is made up off small bhungra',
        'tofu':'It is just a nakli paneer ghatiya hai saala',
        'Dosa':'Ee Sala Cup Namdu'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)

