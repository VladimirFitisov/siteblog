from django.shortcuts import render
# from django.http import HttpResponse #удаляем теперь будим рендерить


def index(request):
    return render(request, 'blog/index.html')



