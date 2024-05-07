from django.db import models

# Create your models here.


class StatusChoice(models.TextChoices):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    class Meta:
        managed = True
        db_table = "vendor"


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=StatusChoice.choices)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = "purchase_order"


class PerformanceRecord(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE
    )  # Link to the Vendor model
    date = models.DateTimeField()  # Date of the performance record
    on_time_delivery_rate = (
        models.FloatField()
    )  # Historical record of the on-time delivery rate
    quality_rating_avg = (
        models.FloatField()
    )  # Historical record of the quality rating average
    average_response_time = (
        models.FloatField()
    )  # Historical record of the average response time
    fulfillment_rate = models.FloatField()  # Historical record of the fulfillment rate

    class Meta:
        managed = True
        db_table = "performance_record"
