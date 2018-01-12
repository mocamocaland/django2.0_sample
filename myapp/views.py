from django.shortcuts import render


def index(request):
    # top page
    context = {
        'name': 'mocamoca',
    }
    return render(request, 'myapp/index.html', context)


def about(request):
    #/aboutpage
    return render(request, 'myapp/about.html')


def info(request):
    # info page
    return render(request, 'myapp/info.html')