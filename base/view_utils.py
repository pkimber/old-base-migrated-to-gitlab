# -*- encoding: utf-8 -*-
from django.conf import settings
from django.utils import timezone


class BaseMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            path=get_path(self.request.path),
            request_path=self.request.path,
            testing=settings.TESTING,
            today=timezone.now(),
        ))
        return context


def get_path(path):
    """Path processing can be used by other views."""
    result = path
    if result == '/':
        result = 'home'
    return result
