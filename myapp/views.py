from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Todo
from .forms import MyForms
from django.contrib import messages



# Create your views here.

def index(request):
    data = Todo.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mycontext': data
    }
    return HttpResponse(template.render(context, request))


def create(request):
    if request.method == 'POST':
        form = MyForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], content=cd['content'], enable=cd['enable'])
            messages.success(request, " Todo Created successfully", 'success')
            return redirect('todo/')

    else:
        form = MyForms()
    return render(request, 'create.html', {'form': form})
