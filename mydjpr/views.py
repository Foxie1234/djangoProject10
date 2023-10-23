from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mydjpr.models import TestModel

def home(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'home.html', context)

def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    number_of_words = len(words)
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text,
                                            'reversedtext': reversed_text, 'number_of_words': number_of_words})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        # обработка POST запроса
        return HttpResponse('Ответ на POST запрос.')
    return render(request, 'login.html')


def index(request):
    ss = TestModel.objects.all()
    print()
    arr = []
    for i in ss: arr.append(i.title)
    m = TestModel()
    m.name = 'Таня'
    m.title = 'Ольшаник'
    m.save()

    return render(request, 'index.html', {"list": arr})
