import pytest
from users.models import User


@pytest.mark.django_db
def test_single_user_factory(user_test_factory):
    user = user_test_factory.create()
    assert user.first_name
    assert user.last_name
    assert user.password
    print(user.password)  # Supposed to get a hashed password
    print(user)  # Supposed to return email
    print(User.objects.all().count())


@pytest.mark.django_db
def test_batch_user_creation(user_test_factory):
    user_list = user_test_factory.create_batch(30)
    assert len(user_list) == 30
    assert user_list[0].password
    print(User.objects.all().count())
