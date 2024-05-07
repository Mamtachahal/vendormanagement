from vendor.models import PurchaseOrder
from rest_framework import serializers

from datetime import datetime


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class PurchaseAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["acknowledgment_date"]

    def save(self, **kwargs):
        instance = self.instance
        instance.acknowledgment_date = datetime.now()

        return super().save(**kwargs)
