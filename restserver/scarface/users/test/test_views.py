from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import UserFactory
from ..models import User

fake = Faker()


class TestUserListTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.url = reverse('user-list')
        self.user_data = model_to_dict(UserFactory.build())
        del self.user_data['last_login']  # Remove unused field

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.user_data)
        assert response.status_code == status.HTTP_201_CREATED

        user = User.objects.get(pk=response.data.get('id'))
        assert user.username == self.user_data.get('username')
        assert check_password(self.user_data.get('password'), user.password)


class TestUserDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_put_request_updates_a_user(self):
        new_first_name = fake.first_name()
        payload = {'first_name': new_first_name}
        response = self.client.put(self.url, payload)
        assert response.status_code == status.HTTP_200_OK

        user = User.objects.get(pk=self.user.id)
        assert user.first_name == new_first_name
