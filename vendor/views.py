from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Min

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets
from vendor.serializers import (VendorSerializer,
                                PurchaseOrderSerializer,
                                HistoricalPerformanceSerializer)

from vendor.models import Vendor,PurchaseOrder,HistoricalPerformance

def home(rquest):
    return HttpResponse("<h1>Vendor Management </h1><br><h2>Api url: http://127.0.0.1:8000/api/<h2")
#Vendors
class VenderViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        vendor.update_performance_metrics()
        vendor.update_historical_performance()
        
        serializer = self.get_serializer(vendor)
        return Response(serializer.data)

#PurchasOrders
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    @action(detail=True, methods=['get'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        
        # Update acknowledgment_date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        
        # Trigger recalculation of average_response_time for associated vendor
        vendor = purchase_order.vendor
        vendor.update_performance_metrics()
        
        return Response({'message': 'Purchase order acknowledged successfully.'})

#VendorHistory
class HistoricalPerformanceView(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
    @action(detail=False, methods=['get'])
    def vh(self, request,pk=None):
        
        unique_data = HistoricalPerformance.objects.values('vendor').annotate(
        latest_date=Min('date'),
        max_on_time_delivery=Min('on_time_delivery_rate'),
        max_quality_rating=Min('quality_rating_avg'),
        max_average_response=Min('average_response_time'),
        max_fulfilment_rate=Min('fulfilement_rate')
        )
        
        return Response(unique_data)