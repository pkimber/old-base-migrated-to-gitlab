# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
import unittest

from django.core.urlresolvers import reverse

from base.url_utils import url_with_querystring


class TestUrlUtils(unittest.TestCase):

    def test_url_with_querystring(self):
        url = url_with_querystring(
            reverse('login'),
            responsible=5,
            scheduled_for=date.today(),
        )
        # /accounts/login/?responsible=5&scheduled_for=2014-09-05
        self.assertIn('/accounts/login/', url)
        self.assertIn('scheduled_for=2014-09-05', url)
        self.assertIn('responsible=5', url)
