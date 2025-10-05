from django.shortcuts import render

def index(request):
    return render(request, 'main_app/index.html')


def my_page(request, name):
    return render(request, f'main_app/{name}.html')