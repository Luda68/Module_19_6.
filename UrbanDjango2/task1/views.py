from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, 'platform.html')


games_list = ['Atomic Heart', 'Mario', 'Cyberpunk', 'PayDay2', 'Dark Souls']


def games(request):
    context = {
        'games': games_list
    }
    return render(request, 'games.html', context)


def cart(request):
    game = games_list[0]
    context = {
        'game': game
    }
    return render(request, 'cart.html', context)

def valid_data(username, password, repeat_password, age, users):
    """Функция для проверки данных пользователя на уникальность, совпадение паролей и возраст."""
    if username in users:
        return 'Пользователь уже существует'
    if password != repeat_password:
        return 'Пароли не совпадают'
    if int(age) < 18:
        return 'Вы должны быть старше 18'
    return None


def sign_up_by_django(request):
    """Форма отправки данных сделанная с помощью Django.forms"""
    users = ['user1', 'user2', 'user3']
    info = {}
    context = {
        'info': info
    }

    if request.method == 'POST':
        form = UserRegister(request.POST)
        # Получаем данные
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            # Проверка данных
            error = valid_data(username, password, repeat_password,
                               age, users)
            if error:
                info['error'] = error
                return render(request, 'registration_page.html', context)
            return HttpResponse(f'Приветствуем, {username}')
    else:
        info['form'] = UserRegister()

    return render(request, 'registration_page.html', context)


def sign_up_by_html(request):
    """Форма отправки данных, сделанная с помощью HTML"""
    users = ['user1', 'user2', 'user3']
    info = {}
    context = {
        'info': info
    }

    if request.method == 'POST':
        # Получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        # Проверка данных
        error = valid_data(username, password, repeat_password,
                           age, users)
        if error:
            info['error'] = error
            return render(request, 'registration_page.html', context)
        return HttpResponse(f'Приветствуем, {username}')

    return render(request, 'registration_page.html', context)


