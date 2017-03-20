# -*- encoding: utf-8 -*-
import time

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils import timezone


class BaseMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            site_name = settings.SITE_NAME
        except:
            site_name = 'base'
        try:
            company_name = settings.COMPANY_NAME
        except:
            company_name = 'KB Software'
        context.update(dict(
            path=get_path(self.request.path),
            request_path=self.request.path,
            testing=settings.TESTING,
            today=timezone.now(),
            site_name=site_name,
            company_name=company_name,
        ))
        return context


def get_path(path):
    """Path processing can be used by other views."""
    result = path
    if result == '/':
        result = 'home'
    return result


class DateSeriesBarChartMixin(object):
    ''' Create a single series bar chart
    In your template include the template snippet

    {% include 'base/_date_series_bar_chart.html' %}

    or a template derived from this one

    in you get_context_data:
        context = super().get_context_data(**kwargs)
        context.update(
            chartdata=self.get_chart_data(
                container="<container name>",
                legend="<series legend>",
                raw_data=[{'x': <date 1>, 'y': value}, ...],
                date_format="<date format e.g."%b %Y">
            )
        )
        return context

    the css for your container should include the following:
    <id of container> {
        width: <required width>px;
        height: <required height>px;
    }
    '''

    def get_chart_data(self, container, legend, raw_data, date_format):
        data=[]
        for key, value in raw_data:
            data.append(
                {'x': int(time.mktime(key.timetuple()) * 1000),'y': value}
            )

        return {
            'container': container,
            'legend': legend,
            'data': data,
            'date_format': date_format,
        }


class RedirectNextMixin:
    """Handle the 'next' parameter on a URL.

    For details, see
    https://www.kbsoftware.co.uk/docs/app-base.html#redirectnextmixin

    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next_url = self.request.GET.get(REDIRECT_FIELD_NAME)
        if not next_url:
            if self.request.method == 'POST':
                next_url = self.request.POST.get('next')
        if next_url:
            context.update({
                REDIRECT_FIELD_NAME: next_url,
            })
        return context
