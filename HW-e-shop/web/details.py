# ! /usr/ bin / python3
import sys
import cgi
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()

sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')

from orm.ProductCatalog import ProductCatalog

product = ProductCatalog.details(data.getvalue('id'))

print("Content-type: text/html;character=UTF-8")

print()

print(f"<h1>{product.name:30}</h1>")
print(f"<h2>{product.price_value} {product.price_unit}</h2>")
print("<hr>")
print("<a href=' /web/add-to-cart.py?id={product_id}'>Add to cart </a>")
