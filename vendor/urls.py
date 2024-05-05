from django.urls import path,include
from rest_framework.routers import DefaultRouter
from vendor.views import (VenderViewSet,PurchaseOrderViewSet,HistoricalPerformanceView)

from vendor import views
router = DefaultRouter()
router.register('vendor',VenderViewSet)
router.register('purchase_orders',PurchaseOrderViewSet)
router.register('vendor_history',HistoricalPerformanceView)

urlpatterns = [
    path("",include(router.urls)),
]
