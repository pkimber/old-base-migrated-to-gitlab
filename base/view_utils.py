# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.conf import settings


class BaseMixin(object):

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context.update(dict(
            path=get_path(self.request.path),
            request_path=self.request.path,
            testing=settings.TESTING,
            today=datetime.today(),
        ))
        return context


def get_path(path):
    """Path processing can be used by other views."""
    result = path
    if result == '/':
        result = 'home'
    return result
