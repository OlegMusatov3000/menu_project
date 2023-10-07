from django.shortcuts import render


def home_view(request):
    active_menu_item = "Home"
    return render(request, 'home.html', {'active_menu_item': active_menu_item})


def about_view(request):
    # Здесь вы можете определить активный пункт меню для страницы about
    active_menu_item = "About"  # Здесь "About" соответствует названию пункта меню в БД
    return render(request, 'about.html', {'active_menu_item': active_menu_item})
