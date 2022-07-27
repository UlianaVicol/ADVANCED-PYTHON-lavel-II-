# ! /usr/ bin / python3
import sys
import cgi
from time import time_ns
import os
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()

sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')
from orm.CartManager import CartManager
from orm.Client import Client

cookie_data = os.environ.get('HTTP_COOKIE')

print("Content-type: text/html;character=UTF-8")
name = data.getvalue('name')
password = data.getvalue('password')

print()

print(
    f"""
    <h1>Sign ADMIN PANEL </h1>

    <form>
        <input name ='name' type='text' placeholder='enter your name...'/><br>
        <input name ='password' type='password' placeholder='enter your password...'/><br>
        <button>Enter</button>
    </form>
    """
)


