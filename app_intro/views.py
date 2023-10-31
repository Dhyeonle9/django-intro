from django.shortcuts import render

# Create your views here.

# request를 받으면 request에 대한 render를 불러오고 index.html을 열어줘
def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '이도현'

    result = { 
        'username': username,

    }
    return render(request, 'hello.html', result)