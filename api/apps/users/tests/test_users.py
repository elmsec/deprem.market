from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase


User = get_user_model()


class UserTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()

        self.superuser = User.objects.create_superuser(
            username="testadminuser")
        self.superuser.set_password("testpassword")
        self.superuser.save()

    def test_user_list(self):
        url = reverse("user-list")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_user_list_as_superuser(self):
        url = reverse("user-list")
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.data["results"][0]["username"], "testuser")
        self.assertEqual(
            response.data["results"][1]["username"], "testadminuser")

    def test_user_list_as_anonymous(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_user_detail(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_user_detail_as_superuser(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testuser")

    def test_user_detail_as_anonymous(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_user_create(self):
        url = reverse("user-register")
        data = {
            "username": "testuser2",
            "password": "testpassword",
            "confirm_password": "testpassword",
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_user_create_as_superuser(self):
        url = reverse("user-register")
        data = {
            "username": "testuser2",
            "password": "testpassword",
            "confirm_password": "testpassword",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["user"]["username"], "testuser2")
        self.assertContains(response, "refresh", status_code=201)
        self.assertContains(response, "access", status_code=201)

    def test_user_create_as_anonymous(self):
        url = reverse("user-register")
        data = {
            "username": "testuser2",
            "password": "testpassword",
            "confirm_password": "testpassword",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["user"]["username"], "testuser2")
        self.assertContains(response, "refresh", status_code=201)
        self.assertContains(response, "access", status_code=201)

    def test_user_update(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {
            "username": "testuser-updated",
            "first_name": "testuser-updated",
            "last_name": "testuser-updated",
            "email": "",
            "password": "testpassword-updated",
            "confirm_password": "testpassword-updated",
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 403)

    def test_user_update_as_superuser(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {
            "username": "testuser-updated",
            "first_name": "testuser-updated",
            "last_name": "testuser-updated",
            "email": "",
            "password": "testpassword-updated",
            "confirm_password": "testpassword-updated",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testuser-updated")
        self.assertEqual(response.data["first_name"], "testuser-updated")

    def test_user_update_as_anonymous(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {
            "username": "testuser-updated",
            "first_name": "testuser-updated",
            "last_name": "testuser-updated",
            "email": "",
            "password": "testpassword-updated",
            "confirm_password": "testpassword-updated",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 401)

    def test_user_partial_update(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {
            "username": "testuser-updated",
            "first_name": "testuser-updated",
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 403)

    def test_user_partial_update_as_superuser(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {
            "username": "testuser-updated",
            "first_name": "testuser-updated",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testuser-updated")
        self.assertEqual(response.data["first_name"], "testuser-updated")

    def test_user_partial_update_as_anonymous(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {
            "username": "testuser-updated",
            "first_name": "testuser-updated",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 401)

    def test_user_delete(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

    def test_user_delete_as_superuser(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_user_delete_as_anonymous(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)
