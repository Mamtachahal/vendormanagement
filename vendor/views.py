from rest_framework import generics
from vendor.models import Vendor, PurchaseOrder, PerformanceRecord
from vendor.serializers import VendorSerializer, VendorPerformanceSerializer


class VendorsAPIView(generics.ListCreateAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorDetailsAPIView(generics.DestroyAPIView, generics.RetrieveUpdateAPIView):
    serializer_class = VendorSerializer
    lookup_field = "id"
    queryset = Vendor.objects.all()


class VendorPerformanceView(generics.RetrieveAPIView):
    serializer_class = VendorPerformanceSerializer
    queryset = Vendor.objects.all()
    lookup_field = "id"
