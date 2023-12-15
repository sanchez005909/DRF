from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient, APITransactionTestCase
from rest_framework import status

from curses.models import Curs, Subscription
from users.models import User


class CursesAPITestCase(APITransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.url = '/curses/'
        self.data = Curs.objects.create(title='Test curs', description='Test curs 1')
        user_create = User.objects.create(email='test1@tes.tes', password='12345', role='moderator')
        self.user = User.objects.get(email='test1@tes.tes')
        client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_curses(self):
        """Тест создания курсов"""
        data = {
            'title': 'Test create curs',
            'description': 'Test create curs 1'
        }
        response = self.client.post(
            self.url,
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data, {'id': 2,
                                         'title': 'Test create curs',
                                         'description': 'Test create curs 1',
                                         'owner': 1,
                                         'lessons_count': 0,
                                         'lessons_': None,
                                         'subscribers': []}
                         )

        self.assertTrue(Curs.objects.all().exists())

    def test_destroy_curs(self):
        # get_ = self.client.get('/curses/3/')
        response = self.client.delete(
            '/curses/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_curs(self):
        response = self.client.get(
            self.url
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'count': 1,
                                           'next': None,
                                           'previous': None,
                                           'results': [
                                               {'id': 1,
                                                'title': 'Test curs',
                                                'description': 'Test curs 1',
                                                'owner': None,
                                                'lessons_count': 0,
                                                'lessons_': None,
                                                'subscribers': []
                                                },
                                           ]
                                           }
                         )

    def test_retrieve_curs(self):
        response = self.client.get(
            '/curses/1/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, {'id': 1,
                                         'title': 'Test curs',
                                         'description': 'Test curs 1',
                                         'owner': None,
                                         'lessons_count': 0,
                                         'lessons_': None,
                                         'subscribers': []
                                         }
                         )

    def test_create_subscription(self):
        # print(User.objects.all().id)
        data = {'user': self.user.id,
                'course': self.data.id
                }

        response = self.client.post(
            '/subcription_create/',
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data, {'user': 1, 'course': 1})

        self.assertTrue(Subscription.objects.all().exists())

    def test_delete_subscription(self):
        data = Subscription.objects.create(user=self.user, course=self.data)
        response = self.client.delete(
            '/subcription_destroy/1/'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Subscription.objects.all().exists())
