from django.shortcuts import render

POSTS = [
    {
        'id': 1,
        'title': 'Первое знакомство с Django',
        'content': 'Django работает по паттерну MVT (Model-View-Template). Это очень удобно!',
        'author': 'admin',
        'date': '2023-10-25',
    },
    {
        'id': 2,
        'title': 'Cookies в вебе',
        'content': 'Cookies позволяют сохранять состояние между запросами. Например, тему оформления.',
        'author': 'user123',
        'date': '2023-10-26',
    },
    {
        'id': 3,
        'title': 'C++ vs Python',
        'content': 'C++ быстрый и компилируемый, а Python гибкий и интерпретируемый.',
        'author': 'guest',
        'date': '2023-10-27',
    },
]

def post_list(request):
    
    context = {
        'posts': POSTS
    }
    
    return render(request, 'blog/post_list.html', context)