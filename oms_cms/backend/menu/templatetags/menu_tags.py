from django import template

from oms_cms.backend.menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('base/tags/menu-item-tag.html', takes_context=True)
def menu_item(context, menu):
    return {"items": MenuItem.objects.filter(menu__name=menu, parent__isnull=True)}
