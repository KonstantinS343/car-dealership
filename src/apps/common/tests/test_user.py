from django.conf import settings
from django.contrib.auth import get_user_model
from django.test.utils import override_settings

from djet import assertions

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from unittest import mock

from djoser.conf import settings as default_settings

from apps.common.conftest import create_user, perform_create_mock

User = get_user_model()


class UserCreateViewTest(
    APITestCase,
    assertions.StatusCodeAssertionsMixin,
    assertions.EmailAssertionsMixin,
    assertions.InstanceAssertionsMixin,
):
    def setUp(self):
        self.base_url = reverse("user-list")  # /auth/users/

    @override_settings(DJOSER=dict(settings.DJOSER, **{"SEND_ACTIVATION_EMAIL": True}))
    def test_post_create_user_with_login_and_send_activation_email(self):
        data = {"username": "john", "email": "john@beatles.com", "password": "secretsecret"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_201_CREATED)
        self.assert_instance_exists(User, username=data["username"])
        self.assert_emails_in_mailbox(1)
        self.assert_email_exists(to=[data["email"]])

        user = User.objects.get(username="john")
        self.assertFalse(user.is_active)

    @override_settings(
        DJOSER=dict(
            settings.DJOSER,
            **{"SEND_ACTIVATION_EMAIL": False, "SEND_CONFIRMATION_EMAIL": True},
        )
    )
    def test_post_create_user_with_login_and_send_confirmation_email(self):
        data = {"username": "john", "email": "john@beatles.com", "password": "secretsecret"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_201_CREATED)
        self.assert_instance_exists(User, username=data["username"])
        self.assert_emails_in_mailbox(1)
        self.assert_email_exists(to=[data["email"]])

        user = User.objects.get(username="john")
        self.assertTrue(user.is_active)

    def test_post_not_create_new_user_if_username_exists(self):
        create_user(username="john")
        data = {"username": "john", "email": "john@beatles.com", "password": "secretsecret"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)

    def test_post_not_register_if_fails_password_validation(self):
        data = {"username": "john", "email": "john@beatles.com", "password": "666"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)

    @override_settings(DJOSER=dict(settings.DJOSER, **{"USER_CREATE_PASSWORD_RETYPE": True}))
    def test_post_not_register_if_password_mismatch(self):
        data = {
            "username": "john",
            "email": "john@beatles.com",
            "password": "secret",
            "re_password": "wrong",
        }
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)

    @mock.patch(
        "djoser.serializers.UserCreateSerializer.perform_create",
        side_effect=perform_create_mock,
    )
    def test_post_return_400_for_integrity_error(self, perform_create):
        data = {"username": "john", "email": "john@beatles.com", "password": "secretsecret"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            [default_settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR],
        )
