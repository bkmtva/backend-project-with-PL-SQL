from atexit import register
# from nis import cat
from django import template
from poll.models import *


register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)
    


@register.inclusion_tag('poll/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    
    return {"cats": cats, "cat_selected": cat_selected}
