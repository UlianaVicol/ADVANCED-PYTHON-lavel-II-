# ! /usr/ bin / python3
import sys
import cgi
from time import time_ns
import os
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()

sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')
cookie_data = os.environ.get('HTTP_COOKIE')

if cookie_data != '':
    cookie_key, cookie_value = cookie_data.split('=')

    if cookie_key != 'admin_id':
        print(f"Refresh: 0; URL=/web/admin/sign-in.py")

print("Content-type: text/html;character=UTF-8")
print()