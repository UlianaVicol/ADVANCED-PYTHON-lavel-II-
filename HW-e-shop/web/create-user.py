# ! /usr/ bin / python3
import sys
import cgi
from time import time_ns
from random import randint
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()

sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')

from orm.CartManager import CartManager
from orm.Client import Client

name = data.getvalue('name')
email = data.getvalue('email')
phone = data.getvalue('phone')
password = data.getvalue('password')
product_id = data.getvalue('id')

id = time_ns() * 10 + randint(0, 9)
client = Client(
    id,
    name,
    email,
    phone,
    False,
    password
    )
client.create()

print(f"Set-cookie: client_id={id};")
print(f"Refresh: 0; URL=/web/add-to-cart.py?id={product_id}")
print("Content-type: text/html;character=UTF-8")

print()
