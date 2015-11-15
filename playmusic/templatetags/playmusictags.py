from django import template
register = template.Library()
@register.filter
def replacetag(value, arg):
	return value.replace(arg, ' ')
