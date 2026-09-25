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
    current_theme = request.COOKIES.get('theme', 'theme-light')
    current_font = request.COOKIES.get('font_size', 'font-normal')

    if request.method == 'POST':
        current_theme = request.POST.get('theme', current_theme)
        current_font = request.POST.get('font_size', current_font)

    context = {
        'posts': POSTS,
        'current_theme': current_theme,
        'current_font': current_font,
    }

    response = render(request, 'blog/post_list.html', context)

    if request.method == 'POST':
        response.set_cookie('theme', current_theme, max_age=31536000)
        response.set_cookie('font_size', current_font, max_age=31536000)

    return response