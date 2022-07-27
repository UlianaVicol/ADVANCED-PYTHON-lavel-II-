# ! /usr/ bin / python3
import sys
import cgi
from time import time_ns
from random  import randint
import os
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()
cookie_data = os.environ.get('HTTP_COOKIE')

sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')
from orm.CartManager import CartManager
from orm.Client import Client

product_id = data.getvalue('id')
CartManager.addItem(product_id)

if cookie_data != '':
    cookie_key, cookie_value = cookie_data.split('=')

    if cookie_key == 'client_id':
        print(f"Refresh: 0; URL=/web/catalog.py")
        client = Client.get(int(cookie_value))
        if client != None:
            pass
else:
    print(f"Refresh: 0; URL=/web/sign-up.py?id={product_id}")

print("Content-type: text/html;character=UTF-8")
print()


















