from django.test import TestCase

from login.tests.scenario import (
    get_user_staff,
    get_user_web,
)


class PermTestCase(TestCase):

    def assert_any(self, url):
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            "status {}: everyone should not have access to '{}'".format(
                response.status_code, url
            )
        )

    def assert_staff_only(self, url):
        self._assert_no_perm(url)
        self._assert_no_web(url)
        self._assert_staff(url)

    def _assert_no_perm(self, url):
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            302,
            "status {}: no user login - "
            "so should not have access to '{}'".format(
                response.status_code, url
            )
        )

    def _assert_no_web(self, url):
        web = get_user_web()
        self.client.login(
            username=web.username, password=web.username
        )
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            302,
            "status {}: user '{}' should not have access "
            "to this url: '{}'".format(
                response.status_code, web.username, url
            )
        )

    def _assert_staff(self, url):
        staff = get_user_staff()
        self.client.login(
            username=staff.username, password=staff.username
        )
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            "status {}: staff user '{}' should have access "
            "to this url: '{}'".format(
                response.status_code, staff.username, url
            )
        )
