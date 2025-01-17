from django.shortcuts import render

def contact(request):
    return render(request, 'contact/index.html')

def message(request):
    return render(request, 'contact/message.html')