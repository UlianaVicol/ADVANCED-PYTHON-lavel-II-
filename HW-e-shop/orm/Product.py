from numpy import prod
import psycopg2
from .Model import Model
# Model
class Product(Model):
    def __init__(self, id, name, price_value, price_unit, bar_code, quantity):
        self.id = id
        self.name = name
        self.price_value = price_value
        self.price_unit = price_unit
        self.bar_code = bar_code
        self.quantity = quantity

    def delete(self):
        sql = "DELETE  FROM \"Product\" WHERE id = {self.id};"
        self.executeUpdateSQL(sql)

    def all(price_sort):
        sql = f"SELECT * FROM \"Product\" ORDER BY price_value {price_sort};"
        product_list = Product.executeFetchSQL(sql)
        products = []
        for product_tuple in product_list:
            product = Product( *product_tuple )
            products.append(product)
        return products

    def get(id):
        sql = f"SELECT * FROM \"Product\" WHERE id = {id};"
        product_list = Product.executeFetchSQL(sql)
        if len(product_list) > 0  : 
            product_tuple = product_list[0]
            product = Product(
                product_tuple[0],
                product_tuple[1],
                product_tuple[2],
                product_tuple[3],
                product_tuple[4],
                product_tuple[5]
            )   
            return product
        else:
            return None


    def create(self):
        sql = f"INSERT INTO \"Product\" (id, name, price_value, price_unit, bar_code, quantity) VALUES ({self.id}, '{self.name}', {self.price_value}, '{self.price_unit}', '{self.bar_code}', {self.quantity});"
        self.executeUpdateSQL(sql)

    def save(self):
        sql = f"UPDATE \"Product\" SET name = '{self.name}', price_value = {self.price_value}, price_unit = '{self.price_unit}', bar_code = '{self.bar_code}', quantity = {self.quantity} WHERE id = {self.id};"
        self.executeUpdateSQL(sql)
  
    def __str__(self):
        return f"Products id:{self.id}"
    def __repr__(self):
        return str(self)