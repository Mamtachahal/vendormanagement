
## Steps ##
1. Clone the project

## Create Virtual Env ##
```
python -m venv myvenv
```

## Activate Virtual Env ##
```
source myvenv/bin/activate
```

## Install All Packages ##
```
pip install -r requirement.txt
```
## Run the server ##

```
python manage.py runserver
```
## Sample Curls ##
1 List vendor 

```
curl --location 'http://127.0.0.1:8000/api/vendors/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```

2 Reterview Vendor 
```
curl --location 'http://127.0.0.1:8000/api/vendors/7/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```

3 Vendor performance 
```
curl --location 'http://127.0.0.1:8000/api/vendors/7/performance/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```

4 Delete vendor 
```
curl --location --request DELETE 'http://127.0.0.1:8000/api/vendors/4/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
5 Update Vendor
```
curl --location --request PUT 'http://127.0.0.1:8000/api/vendors/7/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
6 List Purchase Orders
```
curl --location 'http://127.0.0.1:8000/api/purchase_orders/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
7 Delete Purchase Order
``` 
curl --location --request DELETE 'http://127.0.0.1:8000/api/purchase_orders/7/' 
```



