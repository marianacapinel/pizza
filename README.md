# _pizza_
# Ordering pizzas
This document provides a simple backend Rest API created with Django framework and Python for a web service to order pizzas.

# Functionality

1. Create a order
   - Select between the existing client list. Each client has a unique id, name and address. 
   - Enter date. 
   - Select pizza(s). Pizzas are available with different characteristics: 
     - id: default pizza id. 
     - Name: shows common pizzas like __Margherita__ and __Salami__.
     - Size: Small(30cm) or Large(50cm).
     - Price: from 3€ to 5.5€ depending on the size and the name. 
2. The order can be updated. 
3. The order can be deleted.
4. A list of all orders and orders per client can be shown.


The model designed in Django consist in 3 classes. 

**Class Pizza**: id(generated by default as primary key),name(common pizza names),size(to choose between Small-30cm or Large-50cm) and price. 

**Class Client**: id (generated by default as primary key), name and address. 

**Class Order**: id (generated by default as primary key), client(relationship **one-to-many** with client class: one client can have many orders, but one order can have just one client) and pizzas(relationship **many-to-many**: one pizza can be in many orders and one order can have many pizzas).

The database was created with PostgreSQL and it is named __pizzaservice__. It consists of 4 tables: Pizza, Client, Order, Order_Pizza.

## Run the app

In the cmd go to the file's directory. 
Then type: 

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
``` 


# Run the tests

In the cmd go to the file's directory. 
Then type:

> python manage.py test

The test creates a new order:

'http://127.0.0.1:8000/orders/’
Endpoint tested: Create, update and delete order


## API endpoints

### Title 
Show All Pizzas
>pizza_list
### URL 
/pizzas
### Method 
GET 
### Success Response
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[
    {
        "id": 1,
        "name": "Margherita",
        "size": "Small",
        "price": 3.0
    },
    {
        "id": 2,
        "name": "Margherita",
        "size": "Large",
        "price": 5.0
    },
    {
        "id": 3,
        "name": "Salami",
        "size": "Small",
        "price": 3.5
    },
    {
        "id": 4,
        "name": "Salami",
        "size": "Large",
        "price": 5.5
    },
    {
        "id": 5,
        "name": "Pineapple",
        "size": "Small",
        "price": 3.5
    },
    {
        "id": 6,
        "name": "Pineapple",
        "size": "Large",
        "price": 5.5
    },
]
```
---
### Title 
Show Specific Pizza
>pizza_detail
### URL 
/pizzas/:id 
### Method 
GET
### URL Params 
Required:
``` 
id=[integer] 
example: id=5
```
### Success Response 
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "id": 1,
    "name": "Margherita",
    "size": "Small",
    "price": 3.0
}
```
### Error Response 
```
Code: 404 NOT FOUND
Content: { “detail” : "Not found" }
```
---
### Title 
Show All Clients
>client_list
### URL 
/clients
### Method 
GET 
### Success Response  
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[
    {
        "id": 1,
        "name": "Mariana",
        "address": "Gesundbrunnen"
    },
    {
        "id": 2,
        "name": "Leo",
        "address": "Steglitz"
    },
    {
        "id": 3,
        "name": "Alex",
        "address": "Spandau"
    }
]
```
---
### Title 
Show Specific Client
>client_detail
### URL 
/clients/:id 
### Method 
GET
### URL Params 
Required: 
```
id=[integer] 
example: id=5
```
### Success Response 
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
 {
    "id": 1,
    "name": "Mariana",
    "address": "Gesundbrunnen"
}
```
---
### Title 
Show All Orders and Create New Order
>order_list
### URL 
/orders
### Method 
GET | POST 
### Data Params 
```
{
    "date": [%Y-%m-%d],
    "client": [String],
    "pizzas": [numeric]
}
```
### Success Response  
Create Order Example:
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 7,
    "date": "2018-06-13",
    "client": 3,
    "pizzas": [
        5
    ]
}
```
---
### Title 
Update and delete order
>order_detail
### URL 
/orders/:id 
### Method 
GET | DELETE | PUT
### URL Params 
```
Required: 
id=[integer] 
example: id=2
```
### Data Params 
```
{
    "date": [%Y-%m-%d],
    "client": [String],
    "pizzas": [numeric]
}
```
### Success Response
Update order example:
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "date": "2018-08-01",
    "client": 1,
    "pizzas": [
        1,
        3,
        4,
        5,
        7
    ]
}
```
### Error Response 
```
Code: 400 BAD REQUEST
Content:  {
    "date": [
        "Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]]."
    ]
}
```
--- 
### Title 
Show Orders per Client
>order_clients
### URL 
/orders/client/:id 
### Method 
GET
### URL Params 
```
Required: 
id=[integer] 
example: id=5
```
### Success Response 
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[
    {
        "id": 2,
        "date": "2018-07-28",
        "client": 2,
        "pizzas": [
            1,
            3,
            9
        ]
    },
    {
        "id": 5,
        "date": "2018-07-29",
        "client": 2,
        "pizzas": [
            1,
            3,
            5
        ]
    }
]
```
### Error Response 
```
Code: 404 NOT FOUND
Content: { “detail” : "Not found" }
```

