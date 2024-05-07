from django.test import TestCase
from django.urls import reverse
from vendor.models import PurchaseOrder, Vendor
from datetime import datetime, timedelta


class POAPITestCase(TestCase):
    def setUp(self):
        # self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name="Vendor1",
            contact_details="Contact Details 1",
            address="Address 1",
            vendor_code="VENDOR001",
        )
        self.purchase_order1 = PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=datetime.now(),
            delivery_date=datetime.now() + timedelta(days=6),
            items=[{"name": "Item 1", "price": 10}, {"name": "Item 2", "price": 20}],
            quantity=10,
            status="Pending",
            issue_date=datetime.now(),
        )

    def test_po_list_view(self, curr_len=1):
        response = self.client.get(reverse("po-create-list"))
        self.assertEqual(response.status_code, 200, "Failed to get 200 status code")
        self.assertEqual(len(response.data), curr_len)

    def test_po_create_view(self):
        response = self.client.post(
            reverse("po-create-list"),
            data={
                "po_number": "PO002",
                "vendor": self.vendor.pk,
                "order_date": datetime.now(),
                "delivery_date": datetime.now() + timedelta(days=5),
                "items": [{"name": "Item 3", "price": 30}],
                "quantity": 5,
                "status": "pending",
                "quality_rating": None,
                "issue_date": datetime.now(),
                "acknowledgment_date": None,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.test_po_list_view(2)

    def test_po_details_view(self):
        response = self.client.get(
            reverse("po-detail-update", kwargs={"id": self.purchase_order1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["quantity"], self.purchase_order1.quantity)

    def test_acknowledge_view(self):
        response = self.client.post(
            reverse("po-acknowledge", kwargs={"id": self.purchase_order1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data.get("acknowledgment_date"))

    def test_po_update_view(self):
        po = PurchaseOrder.objects.get(pk=self.purchase_order1.pk)
        data = {
            "po_number": po.po_number,
            "vendor": self.vendor.id,
            "order_date": po.order_date,
            "delivery_date": po.delivery_date,
            "items": po.items,
            "quantity": po.quantity,
            "status": "completed",
            "quality_rating": po.quality_rating,
            "issue_date": po.issue_date,
            "acknowledgment_date": po.acknowledgment_date,
        }
        response = self.client.put(
            reverse("po-detail-update", kwargs={"id": self.purchase_order1.pk}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("status"), "completed")

    def test_delete_view(self):
        response = self.client.delete(
            reverse("po-detail-update", kwargs={"id": self.purchase_order1.pk})
        )
        self.assertEqual(response.status_code, 204)
        response = self.client.get(
            reverse("po-detail-update", kwargs={"id": self.purchase_order1.pk})
        )
        self.assertEqual(response.status_code, 404)
