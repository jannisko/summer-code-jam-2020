from django import template

register = template.Library()


def lookup(array, key):
    key = int(key)
    return array[key]

def img(value):
    return 'images/occupied-'+str(value)+".png"

register.filter(lookup)
register.filter(img)

