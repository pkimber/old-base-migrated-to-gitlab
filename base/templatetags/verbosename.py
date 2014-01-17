from django import template


register = template.Library()


def verbosename(item):
    return item._meta.verbose_name


verbosename.is_safe = True
register.filter(verbosename)
