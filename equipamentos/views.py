from django.shortcuts import render
from django.http import HttpResponse


def equipamentos(request):
    return render(request, 'equipamentos.html')
