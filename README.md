#vendor-management-system-django
Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics

####Prerequisites
Python (version 3.11.7)
Django (version 5.0.4)
##Installation
#1. Clone the repository:
bash:
git clone https://github.com/sachinpatel16/Vendor-management.git
cd project-directory (Vendor-management)
bash:
git clone https://github.com/sachinpatel16/Vendor-management.git
cd project-directory (Vendor-management)

#2.Create a virtual environment:
python -m venv mvenv
source mvenv/bin/activate # For Linux/Mac
mvenv\Scripts\activate # For Windows

#3.Install dependencies:
pip install -r requirements.txt

#4.Database setup:
python manage.py migrate
python manage.py makemigrations vendor
python manage.py migrate vendor
python manage.py createsuperuser

####Usage
#1.Start the server:
python manage.py runserver

#2.Access API endpoints:
####Vendor API: /api/vendor/
Purchase Order API: /api/purchase_orders/
Historical Data API: /api/vendor_history/
Historical Performance API: /api/vendor_history/vh

#After creating user to access token
'/gettoken/' #provide username and password in json eg. { "username":"superuser","password":"superuser" }
I used Postman to test API
once Token is created or received provide it to HEADER
with key as Authorization (eg. key : Authorization) and value as token

####API Endpoints
Vendor API
● POST /api/vendor/: Create a new vendor.
● GET /api/vendor/: List all vendors.
● GET /api/vendor/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendor/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendor/{vendor_id}/: Delete a vendor

● Vendor Performance Endpoint (GET /api/vendor/{vendor_id}/performance)

Purchase Order API
● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order

Vendor Performance Evaluation
● GET /api/vendor/{vendor_id}/performance: Retrieve a vendor's performance metrics

Historical Performance API
GET /api/vendor_history:ALL Data List historical performance for all vendors.
GET /api/vendor_history/vh/:historical performance Analysis for a vendor.

Vendors acknowledge PO
● GET /api/purchase_orders/{po_id}/acknowledge 

####Running Tests

Run the test suite:
python manage.py test