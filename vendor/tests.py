from django.test import TestCase
from django.urls import reverse
from vendor.models import Vendor


class VendorAPITestCase(TestCase):
    def setUp(self):
        # self.client = APIClient()
        self.vendor1 = Vendor.objects.create(
            name="Vendor1",
            contact_details="Contact Details 1",
            address="Address 1",
            vendor_code="VENDOR001",
        )
        self.vendor2 = Vendor.objects.create(
            name="Vendor2",
            contact_details="Contact Details 2",
            address="Address 2",
            vendor_code="VENDOR002",
        )

    def test_vendor_list_view(self, curr_len=2):
        response = self.client.get(reverse("vendor-list"))
        self.assertEqual(response.status_code, 200, "Failed to get 200 status code")
        self.assertEqual(len(response.data), curr_len)

    def test_vendor_create_view(self):
        response = self.client.post(
            reverse("vendor-list"),
            data={
                "name": "Test Vendor",
                "contact_details": "Contact Details 3",
                "address": "Address 3",
                "vendor_code": "VENDOR003",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.test_vendor_list_view(3)

    def test_vendor_update_view(self):
        response = self.client.put(
            reverse("vendor-detail", kwargs={"id": self.vendor1.pk}),
            data={
                "name": "Vendor 1",
                "contact_details": "Contact Details 1",
                "address": "Address 4",
                "vendor_code": "VENDOR001",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("address"), "Address 4")

    def test_vendor_details_view(self):
        response = self.client.get(
            reverse("vendor-detail", kwargs={"id": self.vendor1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.vendor1.name)
