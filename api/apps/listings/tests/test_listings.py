from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from listings.models import Listing, Category


User = get_user_model()


class ListingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()

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

    def test_listing_list(self):
        url = reverse("listing-list")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], "testlisting")

    def test_listing_detail(self):
        url = reverse("listing-detail", kwargs={"pk": self.listing.pk})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "testlisting")

    def test_listing_create(self):
        url = reverse("listing-list")
        data = {
            "title": "testlisting2",
            "slug": "testlisting2",
            "description": "testdescription2",
            "listing_type": "offer",
            "offer_type": "job",
            "category": reverse(
                "category-detail", kwargs={"pk": self.category.pk}),
            "created_by": reverse("user-detail", kwargs={"pk": self.user.pk})
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "testlisting2")

    def test_listing_update(self):
        url = reverse("listing-detail", kwargs={"pk": self.listing.pk})
        data = {
            "title": "testlisting-updated",
            "slug": "testlisting-updated",
            "description": "testdescription-updated",
            "listing_type": "offer",
            "offer_type": "job",
            "category": reverse(
                "category-detail", kwargs={"pk": self.category.pk}),
            "created_by": reverse("user-detail", kwargs={"pk": self.user.pk})
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "testlisting-updated")

    def test_listing_delete(self):
        url = reverse("listing-detail", kwargs={"pk": self.listing.pk})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Listing.objects.count(), 0)

    def test_listing_create_without_login(self):
        url = reverse("listing-list")
        data = {
            "title": "testlisting2",
            "slug": "testlisting2",
            "description": "testdescription2",
            "listing_type": "offer",
            "offer_type": "job",
            "category": self.category.pk,
            "created_by": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Listing.objects.count(), 1)

    def test_listing_update_without_login(self):
        url = reverse("listing-detail", kwargs={"pk": self.listing.pk})
        data = {
            "title": "testlisting-updated",
            "slug": "testlisting-updated",
            "description": "testdescription-updated",
            "listing_type": "offer",
            "offer_type": "job",
            "category": self.category.pk,
            "created_by": self.user.pk,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Listing.objects.count(), 1)

    def test_listing_delete_without_login(self):
        url = reverse("listing-detail", kwargs={"pk": self.listing.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Listing.objects.count(), 1)
