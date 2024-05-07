
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
1. List vendor 

```
curl --location 'http://127.0.0.1:8000/api/vendors/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
2. Create Vendor 
```
curl --location 'http://127.0.0.1:8000/api/vendors/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8' \
--data '  { "name": "suman",
        "contact_details": "9997770396",
        "address": "Noida",
        "vendor_code": "19"
        }'
```


3.  Vendor Detail
```
curl --location 'http://127.0.0.1:8000/api/vendors/7/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```

4. Vendor performance 
```
curl --location 'http://127.0.0.1:8000/api/vendors/7/performance/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```

5. Delete vendor 
```
curl --location --request DELETE 'http://127.0.0.1:8000/api/vendors/4/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
6. Update Vendor
```
curl --location --request PUT 'http://127.0.0.1:8000/api/vendors/8/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8' \
--data '  { "name": "Mamta",
        "contact_details": "9997770396",
        "address": "Noida",
        "vendor_code": "19"
        }'
```


7. Create Purchase Order
```
curl --location 'http://127.0.0.1:8000/api/purchase_orders/' \
--header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'Cache-Control: max-age=0' \
--header 'Connection: keep-alive' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8; tabstyle=html-tab; csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8' \
--header 'Origin: http://127.0.0.1:8000' \
--header 'Referer: http://127.0.0.1:8000/api/purchase_orders/' \
--header 'Sec-Fetch-Dest: document' \
--header 'Sec-Fetch-Mode: navigate' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'Sec-Fetch-User: ?1' \
--header 'Upgrade-Insecure-Requests: 1' \
--header 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Linux"' \
--form 'csrfmiddlewaretoken="UtynLmtHQP0lamvjA64vN1stx5XIBwthnk7wwjhT7ZF8I3Lw9bqe74SsJLSIoKez"' \
--form 'po_number="14"' \
--form 'order_date="2024-05-06T21:12"' \
--form 'delivery_date="2024-05-07T21:12"' \
--form 'items="{\"a\":\"PEN\",\"b\":\"BOOK\"}"' \
--form 'quantity="1"' \
--form 'status="pending"' \
--form 'quality_rating="1"' \
--form 'issue_date="2024-05-08T21:13"' \
--form 'vendor="7"'
```
8. Update Purchase Orders
```
curl --location --request PUT 'http://127.0.0.1:8000/api/purchase_orders/8/' \
--header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'Cache-Control: max-age=0' \
--header 'Connection: keep-alive' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8; tabstyle=html-tab; csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8' \
--header 'Origin: http://127.0.0.1:8000' \
--header 'Referer: http://127.0.0.1:8000/api/purchase_orders/' \
--header 'Sec-Fetch-Dest: document' \
--header 'Sec-Fetch-Mode: navigate' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'Sec-Fetch-User: ?1' \
--header 'Upgrade-Insecure-Requests: 1' \
--header 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Linux"' \
--form 'csrfmiddlewaretoken="UtynLmtHQP0lamvjA64vN1stx5XIBwthnk7wwjhT7ZF8I3Lw9bqe74SsJLSIoKez"' \
--form 'po_number="14"' \
--form 'order_date="2024-05-06T21:12"' \
--form 'delivery_date="2024-05-07T21:12"' \
--form 'items="{\"a\":\"PENS\",\"b\":\"BOOKS\"}"' \
--form 'quantity="1"' \
--form 'status="pending"' \
--form 'quality_rating="1"' \
--form 'issue_date="2024-05-08T21:13"' \
--form 'vendor="7"'
```
9. List Purchase Orders
```
curl --location 'http://127.0.0.1:8000/api/purchase_orders/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
10. Delete Purchase Order
``` 
curl --location --request DELETE 'http://127.0.0.1:8000/api/purchase_orders/7/' 
```
11. Detail purchase order
```
curl --location 'http://127.0.0.1:8000/api/purchase_orders/7/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```
12. Vendore acknowledgment date

```
curl --location --request POST 'http://127.0.0.1:8000/api/purchase_orders/8/acknowledge/' \
--header 'Cookie: csrftoken=DEvrnCHkTpr8bbQ6mknUsjhtExIEMdOQ6v4A8zvwaz6VJS6jVpJDMmHsQdDEzrz8'
```

