from django.contrib import admin

# Register your models here.
from vendor.models import Vendor,PurchaseOrder,HistoricalPerformance

class VenderAdmin(admin.ModelAdmin):
    list_display = ['id','name','contect_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfilement_rate']

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id','po_number','vendor','items','quantity','status','quality_rating','order_date','acknowledgment_date','issue_date','delivery_date']

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['id','vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfilement_rate']

admin.site.register(Vendor,VenderAdmin)
admin.site.register(PurchaseOrder,PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance,HistoricalPerformanceAdmin)