from django.urls import path
from vendor import views

urlpatterns=[
    path('vendors/',views.VendorsAPIView.as_view()),
    path('vendors/<int:id>/',views.VendorDetailsAPIView.as_view()),
    path('vendors/<int:id>/performance/',views.VendorPerformanceView.as_view()),
    # path('/api/vendors/{vendor_id}/performance',views.VendorPerformanceView)
]