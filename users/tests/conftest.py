import pytest
from pytest_factoryboy import register
from .factories import UserFactory

register(factory_class=UserFactory)


@pytest.fixture
def user_test_factory(user_factory):
    return user_factory
