from django.shortcuts import render
from .forms import ContactForm




# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form_class = ContactForm
    return render(request, 'contact.html', {'form':form_class})
