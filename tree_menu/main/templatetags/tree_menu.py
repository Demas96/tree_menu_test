from django import template
from ..models import Menu


register = template.Library()


@register.inclusion_tag('main/view_menu.html')
def draw_menu(name: str):
    if name == 'main_menu' or name is None:
        menu = Menu.objects.filter(parent=None)
        return {'menu': menu, 'type': 0}
    else:
        menu = Menu.objects.all().order_by('parent_id')
        cur_menu = menu.filter(name=name)[0]
        menu_new = []
        par = cur_menu
        try:
            cur_child = menu.filter(parent=cur_menu)[0]
        except:
            cur_child = cur_menu
        ser = 0
        check = False
        while True:
            for i in menu.filter(parent=par).order_by('serial_number'):
                if i.serial_number > ser:
                    if i == cur_child.parent:
                        check = True
                        menu_new.insert(ser, i)
                    elif check and ser != 0:
                        menu_new.append(i)
                    else:
                        menu_new.insert(ser, i)
                elif i.serial_number < ser or ser == 0:
                    if check:
                        menu_new.append(i)
                    else:
                        menu_new.insert(ser, i)
                ser = i.serial_number
            try:
                par = par.parent
                if check:
                    cur_child = cur_child.parent
                check = False
                ser = 0
            except:
                break

        return {'menu': menu_new, 'type': 1}

