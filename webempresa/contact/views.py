from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = contact_form(data=request.POST)
    