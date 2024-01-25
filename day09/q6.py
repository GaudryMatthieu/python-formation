#Given a JSON file with customer data, create a Customer class to store and manipulate the data.

import json

class Customer:
    def __init__(self, customer_data):
        self.id = customer_data.get('id')
        self.last_name = customer_data.get('last_name')
        self.first_name = customer_data.get('first_name')
        self.address = customer_data.get('address')
        self.email = customer_data.get('email')
        self.phone = customer_data.get('phone')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_info(self):
        print(f"Customer ID: {self.id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Address: {self.address['street']}, {self.address['city']}, {self.address['postal_code']}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

json_data = '''
{
  "id": 1,
  "last_name": "Dupont",
  "first_name": "Jean",
  "address": {
    "street": "123 Republic Street",
    "city": "Paris",
    "postal_code": "75001"
  },
  "email": "jean.dupont@email.com",
  "phone": "+33 123 456 789"
}
'''

customer_data = json.loads(json_data)

customer = Customer(customer_data)

customer.display_info()
