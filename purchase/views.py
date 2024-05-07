from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from vendor.models import Vendor, PurchaseOrder, PerformanceRecord
from purchase.serializers import PurchaseSerializer, PurchaseAcknowledgeSerializer


class PurchaseAPIView(generics.ListCreateAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        vendor = self.request.GET.get("vendor")
        queryset = PurchaseOrder.objects.all()
        if vendor:
            queryset = queryset.filter(vendor__id=vendor)
        return queryset


class PurchaseDetailsAPIView(generics.DestroyAPIView, generics.RetrieveUpdateAPIView):
    serializer_class = PurchaseSerializer
    lookup_field = "id"
    queryset = PurchaseOrder.objects.all()


class PurchaseAcknowledgeview(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = PurchaseAcknowledgeSerializer
    queryset = PurchaseOrder.objects.all()
    lookup_field = "id"

    def post(self, request, *args, **kwargs):

        return super().put(request, *args, **kwargs)
