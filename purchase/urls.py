from django.urls import path
from purchase import views

urlpatterns = [
    path("purchase_orders/", views.PurchaseAPIView.as_view(), name="po-create-list"),
    path(
        "purchase_orders/<int:id>/",
        views.PurchaseDetailsAPIView.as_view(),
        name="po-detail-update",
    ),
    path(
        "purchase_orders/<int:id>/acknowledge/",
        views.PurchaseAcknowledgeview.as_view(),
        name="po-acknowledge",
    ),
]
