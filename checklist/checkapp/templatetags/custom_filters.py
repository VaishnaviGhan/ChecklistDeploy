# checkapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_item_by_index')
def get_item_by_index(lst, index):
    return lst[index]
