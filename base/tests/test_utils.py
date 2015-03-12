# -*- encoding: utf-8 -*-
from django.test import TestCase

from login.tests.factories import (
    TEST_PASSWORD,
    UserFactory,
)
from login.tests.scenario import (
    get_user_staff,
    get_user_web,
)


class PermTestCase(TestCase):

    def setup_users(self):
        """Using factories - set-up users for permissions test cases."""
        UserFactory(
            username='admin',
            email='admin@pkimber.net',
            is_staff=True,
            is_superuser=True
        )
        UserFactory(username='staff', email='staff@pkimber.net', is_staff=True)
        UserFactory(
            username='web', email='web@pkimber.net',
            first_name='William', last_name='Webber'
        )

    def assert_anon(self, url):
        """only anonymous users should have access to this url"""
        self.assert_any(url)
        self._assert_no_staff(url)
        self._assert_no_web(url)

    def assert_any(self, url):
        """all users (logged in or not) should have access to this url"""
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            "status {}: everyone should have access to '{}'".format(
                response.status_code, url
            )
        )

    def assert_logged_in(self, url):
        self._assert_no_perm(url)
        self._assert_web(url)

    def assert_staff_only(self, url):
        """only members of staff should have access to this URL"""
        self._assert_no_perm(url)
        self._assert_no_web(url)
        self._assert_staff(url)

    def _assert_no_perm(self, url):
        """a user who is not logged in should not have access to this URL"""
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

    def _assert_no_staff(self, url):
        """a member of staff should not have access to this url"""
        user = self.login_staff()
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            302,
            "status {}: user '{}' should not have access "
            "to this url: '{}'".format(
                response.status_code, user.username, url
            )
        )

    def _assert_no_web(self, url):
        """a user who is logged in should not have access to this url"""
        user = self.login_web()
        response = self.client.get(url)
        self.assertIn(
            response.status_code,
            (302, 403),
            "status {}: user '{}' should not have access "
            "to this url: '{}'".format(
                response.status_code, user.username, url
            )
        )

    def _assert_staff(self, url):
        staff = self.login_staff()
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            "status {}: staff user '{}' should have access "
            "to this url: '{}'".format(
                response.status_code, staff.username, url
            )
        )

    def _assert_web(self, url):
        """check that a logged in user can view the url"""
        user = self.login_web()
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            "status {}: web user '{}' (logged in) should have access "
            "to this url: '{}'".format(
                response.status_code, user.username, url
            )
        )

    def _login_user(self, user):
        self.assertTrue(
            self.client.login(username=user.username, password='letmein'),
            "Cannot login user '{}', password '{}'.".format(
                user.username, TEST_PASSWORD
            )
        )
        return user

    def login_staff(self):
        return self._login_user(get_user_staff())

    def login_web(self):
        return self._login_user(get_user_web())
