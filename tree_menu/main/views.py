from django.shortcuts import render



def menu(request):
    name_menu = request.GET.get("name")
    data = {
        'name_menu': name_menu
    }
    return render(request, 'main/menu.html', context=data)
