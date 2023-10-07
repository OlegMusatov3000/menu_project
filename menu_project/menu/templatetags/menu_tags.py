from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    try:
        menu_items = MenuItem.objects.filter(title=menu_name).order_by('pk')
    except MenuItem.DoesNotExist:
        return ""

    def render_menu_item(item):
        children = MenuItem.objects.filter(parent=item).order_by('pk')
        if children:
            return f'<li><a href="{item.url}">{item.title}</a><ul>{"".join(render_menu_item(child) for child in children)}</ul></li>'
        else:
            return f'<li><a href="{item.url}">{item.title}</a></li>'

    menu_html = "".join(render_menu_item(item) for item in menu_items)
    return f'<ul>{menu_html}</ul>'
