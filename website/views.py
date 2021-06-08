from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')