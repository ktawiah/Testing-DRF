import factory
import pytest
from faker import Faker
from users.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    id = factory.LazyFunction(fake.uuid4)
    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyAttribute(lambda obj: fake.unique.email())
    is_staff = False
    is_active = True

    @factory.post_generation
    def password(self, created, extracted, **kwargs):
        if not created:
            return
        elif extracted:
            self.set_password(extracted)
        else:
            self.set_password(fake.password())
