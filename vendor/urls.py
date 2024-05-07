from django.urls import path
from vendor import views

urlpatterns = [
    path("vendors/", views.VendorsAPIView.as_view(), name="vendor-list"),
    path(
        "vendors/<int:id>/", views.VendorDetailsAPIView.as_view(), name="vendor-detail"
    ),
    path(
        "vendors/<int:id>/performance/",
        views.VendorPerformanceView.as_view(),
        name="vendor-performance",
    ),
]
