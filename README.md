#  Online Shop API

Django + Django Rest Framework asosida yaratilgan Online Shop backend loyihasi.

---

## Texnologiyalar

- Python
- Django
- Django Rest Framework (DRF)
- JWT Authentication
- SQLite3
- Swagger / Redoc

---

## Authentication

JWT asosida ishlaydi.

### Register
POST `/api/auth/register/`

### Login
POST `/api/auth/login/`

### Logout
POST `/api/auth/logout/`

### Profile
GET `/api/auth/profile/`

### Profile Update
PUT/PATCH `/api/auth/profile/update/`

### Password Reset
PATCH `/api/auth/profile/reset-pass/`

---

## Product API

GET `/api/products/`  
GET `/api/products/{id}/`  
POST `/api/products/create/` (admin)  
PUT/PATCH `/api/products/{id}/update/` (admin)  
DELETE `/api/products/{id}/delete/` (admin)  
GET `/api/products/search/?q=...`

---

## Comment API

GET `/api/products/{id}/comments/`  
POST `/api/products/{id}/comments/`  
PUT/PATCH `/api/products/comments/{id}/update/`  
DELETE `/api/products/comments/{id}/delete/`  
GET `/api/products/comments/`

---

## Cart API

GET `/api/cart/`  
POST `/api/cart/add/`  
POST `/api/cart/remove/`  
POST `/api/cart/clear/`  
PUT/PATCH `/api/cart/update/`

---

## Order API

POST `/api/order/create/`  
GET `/api/orders/`  
GET `/api/orders/{id}/`  
PATCH `/api/orders/{id}/status/` (admin)  
DELETE `/api/orders/{id}/cancel/`

---

## API Documentation

Swagger:
