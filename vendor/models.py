from django.db import models
from django.utils import timezone
from django.db.models import Avg, Count
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contect_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50,unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfilement_rate = models.FloatField(default=0)
        
    
    def update_performance_metrics(self):
        # Calculate On-Time Delivery Rate
        completed_orders = self.purchase_order.filter(status='completed')
        total_completed_orders = completed_orders.count()
        print("total Order",total_completed_orders)
        if total_completed_orders > 0:
            on_time_deliveries = completed_orders.filter(delivery_date__lte=timezone.now()).count()
            # print("com",on_time_deliveries)
            # print("time",timezone.now())
            self.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100
        else:
            self.on_time_delivery_rate = 0

        # Calculate Quality Rating Average
        completed_orders_with_rating = completed_orders.exclude(quality_rating=None)
        self.quality_rating_avg = completed_orders_with_rating.aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0

        # Calculate Average Response Time
        completed_orders_with_acknowledgment = completed_orders.exclude(acknowledgment_date=None)
        if completed_orders_with_acknowledgment.exists():
            avg_response_time = completed_orders_with_acknowledgment.aggregate(avg_response=Avg(models.F('issue_date') - models.F('acknowledgment_date')))['avg_response']
            if avg_response_time is not None:
                self.average_response_time = avg_response_time.total_seconds() / 3600  # Convert to hours
            else:
                self.average_response_time = 0
        else:
            self.average_response_time = 0
        
        # Calculate Fulfilment Rate
        total_orders = self.purchase_order.count()
        # print("total Order:",total_orders)
        # print("complate",completed_orders.count())
        if total_orders > 0:
            successful_orders = completed_orders.filter(quality_rating__isnull=False)
            # print("success o:",successful_orders.count())
            self.fulfilement_rate = (successful_orders.count() / total_orders) * 100
            # print("full fill:",self.fulfilement_rate)    
        else:
            self.fulfilment_rate = 0
            
        self.save()
    
    def update_historical_performance(self):
        # Create HistoricalPerformance instance and save it
        HistoricalPerformance.objects.get_or_create(
            vendor=self,
            on_time_delivery_rate=self.on_time_delivery_rate,
            quality_rating_avg=self.quality_rating_avg,
            average_response_time=self.average_response_time,
            fulfilement_rate=self.fulfilement_rate
        )
    
    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    po_number = models.CharField(max_length=252,unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name='purchase_order')
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='pending')
    quality_rating = models.FloatField(null=True,blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)
    issue_date = models.DateTimeField(null=True,blank=True)
    delivery_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f"PO #{self.po_number}"

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfilement_rate = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.vendor} - {self.date}"
