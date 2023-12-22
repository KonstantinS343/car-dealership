import pytest

from django.contrib.auth import get_user_model
from django.db import IntegrityError

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ddf import G

from apps.common.models import User


@pytest.fixture(scope='function')
def user(db, user_type) -> User:
    user = G(User, user_type=user_type)
    return user


@pytest.fixture(scope='function')
def api_client(user) -> APIClient:
    refresh = RefreshToken.for_user(user)
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client


def create_user(use_custom_data=False, **kwargs):
    data = (
        {"username": "john", "password": "secret", "email": "john@beatles.com"}
        if not use_custom_data
        else {
            "custom_username": "john",
            "password": "secret",
            "custom_email": "john@beatles.com",
            "custom_required_field": "42",
        }
    )
    data.update(kwargs)
    user = get_user_model().objects.create_user(**data)
    user.raw_password = data["password"]
    return user


def perform_create_mock(x):
    raise IntegrityError
