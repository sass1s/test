# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
    return render(request, 'learn/index.html', {'form': form})


def home(request):
    context = dict()
    context['string'] = '实验楼'
    context['TutorialList'] = ['HTML', 'CSS', 'jQuery', 'Python', 'Django']
    return render(request, 'learn/home.html', context)


def add(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))
