from django.shortcuts import render

import requests
from django.http import JsonResponse

def create_lead_in_zoho(request):
    access_token = "1000.26551d85a1ada1c7ff8790c2bcf3ec1e.6a6ee96704da5a1399f8d3e2c3a26f0b"

    url = "https://www.zohoapis.in/crm/v2/Leads"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }

    lead_data = {
        "data": [
            {
                "Company": "Wipro Technologies",
                "Last_Name": "Naidu",
                "First_Name": "Sai",
                "Email": "sai@example.com",
                "Phone": "9876543210"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=lead_data)
    return JsonResponse(response.json())

