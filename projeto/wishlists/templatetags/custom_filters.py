from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplica o valor pelo argumento fornecido."""
    return value * arg
