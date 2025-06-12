# myzohoapp
# 🧩 Zoho CRM Integration with Django

This project demonstrates how to integrate **Zoho CRM** with a **Django web application** using OAuth 2.0 authentication.

It includes full functionality to:
- Authenticate with Zoho via OAuth2
- Exchange the authorization code for access/refresh tokens
- Use the access token to **create a lead** in Zoho CRM

---

## 🚀 Features

✅ OAuth 2.0 Authorization Code Flow  
✅ Access and Refresh Token Handling  
✅ Create a Lead via Zoho CRM REST API  
✅ Django Views to Handle Authentication and API Integration

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Django 3/4**
- **Zoho CRM APIs**
- `requests` for API communication

---

## 🔐 OAuth Flow Overview

1. User clicks an **Authorization URL** to authenticate with Zoho.
2. Zoho redirects back to your Django app with a `code`.
3. Your app exchanges the `c

