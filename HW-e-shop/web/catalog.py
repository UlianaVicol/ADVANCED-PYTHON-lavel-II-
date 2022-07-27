import sys
import cgi
sys.path.append('D:\\uliana\\PYTHON-ADVANCED\\LECTIA-7-E-SHOP--POSTGRES-BASICS\\HW-SHOP-POSTGRESQL-BASICS\\HW-e-shop')

from orm.ProductCatalog import ProductCatalog

data = cgi.FieldStorage()
price_sort = data.getvalue('price_sort')
products = ProductCatalog.index(price_sort if price_sort != None else "asc")

print("Content-type: text/html;character=UTF-8")

print()

print("<h2>sort by price : <a href='/web/catalog.py?price_sort=asc'> v </a> <a href='/web/catalog.py?price_sort=desc'> ^ </a> </h2>" )
for product in products:
    print(f"<h2>{product.name}</h2>")
    print(f"<p><strong>{product.price_value}</strong>{product.price_unit}</p>")
    print(f"<p><a href=' /web/details.py?id={product.id}'>details</a></p>")
    print("<hr>")

