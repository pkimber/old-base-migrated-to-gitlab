# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.http import urlencode


def url_with_querystring(path, **kwargs):
    """Create a URL with a query string.

    # e.g.
    from base.url_utils import url_with_querystring
    url = url_with_querystring(
        reverse(order_add),
        responsible=employee.id,
        scheduled_for=datetime.date.today(),
    )
    >>> http://localhost/order/add/?responsible=5&scheduled_for=2011-03-17

    From:
    http://stackoverflow.com/questions/2778247/how-do-i-construct-a-django-reverse-url-using-query-args#answer-5341769

    """
    if kwargs:
        return path + '?' + urlencode(kwargs)
    else:
        return path
