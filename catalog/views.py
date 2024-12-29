from django.shortcuts import render


def home_page(request):
    return render(request, 'catalog/src/home.html')


def contacts_page(request):
    return render(request, 'catalog/src/contacts.html')