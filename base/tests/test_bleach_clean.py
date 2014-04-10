# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from base.form_utils import bleach_clean


class TestBleachClean(unittest.TestCase):

    def test_default(self):
        description = 'Hot, hot, hot...'
        self.assertEquals(
            'Hot, hot, hot...',
            bleach_clean(description)
        )

    def test_image(self):
        description = (
            '<img alt="" src="http://rodgersindexlarge.jpg" '
            'style="float:right; height:90px; width:160px"/>'
        )
        clean = bleach_clean(description)
        self.assertIn('<img', clean)
        self.assertIn('src', clean)
        self.assertIn('style', clean)
        self.assertIn('float', clean)
        self.assertIn('right', clean)
        self.assertIn('height', clean)
        self.assertIn('width', clean)
        self.assertIn('alt', clean)

    def test_link(self):
        description = (
            '<a target="_blank" href="http://bbc.co.uk">http://bbc.co.uk</a>'
        )
        clean = bleach_clean(description)
        self.assertIn('<a', clean)
        self.assertIn('href', clean)
        self.assertIn('target', clean)

    def test_strong(self):
        description = 'Hot, <strong>hot</strong>, hot...'
        self.assertEquals(
            'Hot, <strong>hot</strong>, hot...',
            bleach_clean(description)
        )

    def test_youtube(self):
        description = (
            '<iframe width="640" height="360" '
            'src="//www.youtube.com/embed/UB-DhUIvcac?rel=0" '
            'frameborder="0" allowfullscreen=""></iframe>'
        )
        clean = bleach_clean(description)
        self.assertIn('<iframe', clean)
        self.assertIn('allowfullscreen', clean)
        self.assertIn('frameborder', clean)
        self.assertIn('height', clean)
        self.assertIn('src', clean)
        self.assertIn('width', clean)
