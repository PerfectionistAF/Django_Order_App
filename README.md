# Django_Order_App

## PolutrySync Task 1: Schema

#### User: Abstract class

#### Company: class inheriting from User 

```
Company (1)_________ (*) User
Company (1)_________ (*) Product
Company (1)_________ (*) Order
Product (1)_________ (*) Order
Order (1) __________ (1) Product
``` 

## Installation: 
```
Start with the code either cloned or downloaded as .zip from this repository. 
Another .zip copy shall be attached via email. Check all __init__ , requirement and settings files before makemigrations. In case of authentication errors, turn off your firewall.
```

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Test Steps:

#### Step 1: 
Start at admin, create the users and give them their roles

#### Step 2: 
Log in as a user, then start either adding companies, products, orders

#### Step 3: 
You can use the api/<endpoint> that view the orders or the products as serialized requests

#### Step 4: 
You can go back to the user admin page to edit/delete your companies, orders, products.

#### Step 4.1: 
You can also export selected products or selected orders as .csv files

## Demo Video



https://github.com/user-attachments/assets/5e59afc8-9ade-4af9-9718-03e690c2fbaf



## Issues:

Major issue with schema involving Many:Many relationship between Orders and Products, 
Orders containing several products aren't serialized correctly

