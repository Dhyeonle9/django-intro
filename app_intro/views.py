from django.shortcuts import render
import random
from faker import Faker

# request를 받으면 request에 대한 render를 불러오고 index.html을 열어줘
def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '이도현'

    result = { 
        'username': username,

    }
    return render(request, 'hello.html', result)

def dinner(request):
    menus = ['라면', '김밥', '떡볶이']
    pick = random.choice(menus)

    result = {
        'pick': pick
    }
    return render(request, 'dinner.html', result)
    
    # 아래같은 코드는 넣어야할 값이 많아질 때 유지보수에 불편
    # return render(request, 'dinner.html', {'pick': pick, })

def lotto(request):
    numbers = range(1, 46)
    lotto_number = random.sample(numbers, 6)
    
    result = {
        'lotto_number': lotto_number,
    }
    return render(request, 'lotto.html', result)

def greeting(request, name):

    result = {
        'name': name,
    }
    return render(request, 'greeting.html', result)

def cube(request, num):
    result = {
        'num': num,
        'cube': num ** 3,
    }
    return render(request, 'cube.html', result)

def posts(request):
    posts = []

    fake = Faker()
    
    for i in range(100):
        posts.append(fake.text())

    result = {
        'posts': posts,



    }
    return render(request, 'posts.html', result)