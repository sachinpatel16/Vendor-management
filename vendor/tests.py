from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.urls import reverse

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample data
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contect_details='Contact Details',
            address='Address',
            vendor_code='V001',
        )

        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            po_number='PO001',
            items={'item1': 'description1'},
            quantity=10,
            status='completed'
        )

        HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.9,
            quality_rating_avg=4.5,
            average_response_time=24,
            fulfilement_rate=0.95
        )

    def test_vendor_api(self):
        # Test create vendor API
        
        url1 = '/api/vendor/'
        url2 = f'/api/vendor/{self.vendor.id}/'
        #POST
        data = {
            'name': 'New Vendor',
            'contect_details': 'New Contact Details',
            'address': 'New Address',
            'vendor_code': 'V002'
        }
        response = self.client.post(url1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        #GET ALL
        response = self.client.get(url1)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        #GET
        response = self.client.get(url2)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        #PATCH
        data = {
            'name': 'Updated Vendor'
            }
        response = self.client.patch(url2,data ,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get(id=self.vendor.id).name,'Updated Vendor')
        
        #PUT
        data = {
            'name': 'Update Vendor',
            'contect_details': 'Update Contact Details',
            'address': 'Update Address',
            'vendor_code': 'U002'
        }
        response = self.client.put(url2,data ,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get(id=self.vendor.id).name,'Update Vendor')
        self.assertEqual(Vendor.objects.get(id=self.vendor.id).contect_details,'Update Contact Details')
        self.assertEqual(Vendor.objects.get(id=self.vendor.id).address,'Update Address')
        self.assertEqual(Vendor.objects.get(id=self.vendor.id).vendor_code,'U002')
        
        #DELETE
        response = self.client.delete(url2)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_purchase_order_api(self):
        # Test create purchase order API
        url1 = '/api/purchase_orders/'
        url2 = f'/api/purchase_orders/{self.purchase_order.id}/'
        
        #POST
        data = {
            'vendor': self.vendor.id,
            'po_number': 'PO002',
            'items': {'item1': 'description1'},
            'quantity': 10,
            'status': 'pending'
        }
        response = self.client.post(url1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        #GET ALL
        response = self.client.get(url1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #DELET
        response = self.client.delete(url2)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_historical_performance_api(self):
        # Test historical performance API
        historical_performance_url = '/api/vendor_history/'
        response = self.client.get(historical_performance_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(historical_performance_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        # Add more tests as needed

