from django import template

register = template.Library()


@register.filter(is_safe=True)
def div_list(value, arg):
    """Returns a list of numbers in a given range which are divisible by an arg number"""
    result_list = []
    for i in range(int(value)):
        if i % arg == 0:
            result_list.append(i)
    return result_list
