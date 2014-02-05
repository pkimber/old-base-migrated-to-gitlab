import unittest

from base.form_utils import bleach_clean


class TestBleachClean(unittest.TestCase):

    def test_default(self):
        description='Hot, hot, hot...'
        self.assertEquals(
            'Hot, hot, hot...',
            bleach_clean(description)
        )

    def test_strong(self):
        description='Hot, <strong>hot</strong>, hot...'
        self.assertEquals(
            'Hot, <strong>hot</strong>, hot...',
            bleach_clean(description)
        )
