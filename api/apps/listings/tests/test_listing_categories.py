from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from listings.models import Listing, Category


User = get_user_model()


class ListingCategoryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()

        self.superuser = User.objects.create_superuser(
            username="testadminuser")
        self.superuser.set_password("testpassword")
        self.superuser.save()

        self.category = Category.objects.create(name="testcategory")
        self.listing = Listing.objects.create(
            title="testlisting",
            slug="testlisting",
            description="testdescription",
            listing_type="offer",
            offer_type="job",
            category=self.category,
            created_by=self.user,
        )

    def test_listing_category_list(self):
        url = reverse("category-list")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["name"], "testcategory")

    def test_listing_category_detail(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "testcategory")

    def test_listing_category_create(self):
        url = reverse("category-list")
        data = {
            "name": "testcategory2",
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_listing_category_update(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        data = {
            "name": "testcategory-updated",
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 403)

    def test_listing_category_delete(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

    def test_listing_category_list_without_login(self):
        url = reverse("category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["name"], "testcategory")

    def test_listing_category_detail_without_login(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "testcategory")

    def test_listing_category_create_without_login(self):
        url = reverse("category-list")
        data = {
            "name": "testcategory2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 401)

    def test_listing_category_partial_update_without_login(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        data = {
            "name": "testcategory-updated",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 401)

    def test_listing_category_update_without_login(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        data = {
            "name": "testcategory-updated",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 401)

    def test_listing_category_delete_without_login(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

    def test_listing_category_list_as_superuser(self):
        url = reverse("category-list")
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["name"], "testcategory")

    def test_listing_category_detail_as_superuser(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "testcategory")

    def test_listing_category_create_as_superuser(self):
        url = reverse("category-list")
        data = {
            "name": "testcategory2",
            "slug": "testcategory2",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "testcategory2")

    def test_listing_category_partial_update_as_superuser(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        data = {
            "name": "testcategory-updated",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "testcategory-updated")

    def test_listing_category_update_as_superuser(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        data = {
            "name": "testcategory-updated",
            "slug": "testcategory-updated",
        }
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "testcategory-updated")
        self.assertEqual(response.data["slug"], "testcategory-updated")

    def test_listing_category_delete_as_superuser(self):
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        self.client.login(username="testadminuser", password="testpassword")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
