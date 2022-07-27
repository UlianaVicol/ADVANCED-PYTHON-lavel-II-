# ! /usr/ bin / python3
import sys
import cgi
from time import time_ns
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()

sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')

from orm.CartManager import CartManager
from orm.Client import Client

product_id = data.getvalue('id')
CartManager.addItem(product_id)

print("Content-type: text/html;character=UTF-8")

print()

print(
    f"""
    <h1> You must sign up to continy</h1>

    <form action='/web/create-user.py'>
        <input name ='name' type='text' placeholder='enter your name...'/><br>
        <input name ='email' type='text' placeholder='enter your email...'/><br>
        <input name ='phone' type='text' placeholder='enter your phone...'/><br>
        <input name ='password' type='password' placeholder='enter your password...'/><br>
        <input name='id' type='hidden' value='{product_id}'>
        <button > Sign Up</button>
    </form>
    """
)