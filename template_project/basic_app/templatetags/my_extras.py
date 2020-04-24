from django import template

register=template.Library()
@register.filter(name='cut') #this is the another custom filter registration method

def cut(value,arg):
	"""
	this cuts out all values of "arg" from the string!

	"""
	return value.replace(arg,'') #this is .replace method of python using this method we can do string operation

#register.filter('cut', cut) 

#the first one is going to be the string that i call the function when i use the template tag
#2ns cut is function itself
# using this filter i mean cut function i can remon the content what ever i want