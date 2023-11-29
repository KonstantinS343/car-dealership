import pytest

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
