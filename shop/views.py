from django.shortcuts import render


def shop(request):
    return render(request, 'shop/index.html')

def search(request):
    return render(request, 'shop/index.html')