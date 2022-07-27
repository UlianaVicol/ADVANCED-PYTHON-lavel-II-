import psycopg2
from .Model import Model 
class Client(Model):

    def __init__(self, id, name, email, phone, is_vip, password):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.is_vip = is_vip
        self.password = password

    def create(self):
        sql = f"INSERT INTO \"Client\" (id, name, email, phone, is_vip, password) VALUES ({self.id}, '{self.name}', '{self.email}', '{self.phone}', {self.is_vip}, '{self.password}');"
        self.executeUpdateSQL(sql)
        
    def get(id):
        sql = f"SELECT * FROM \"Client\" WHERE id = {id};"
        client_list = Client.executeFetchSQL(sql)
        if len(client_list) > 0  : 
            client_tuple = client_list[0]
            client = Client(
                client_tuple[0],
                client_tuple[1],
                client_tuple[2],
                client_tuple[3],
                client_tuple[4],
                client_tuple[5]
            )   
            return client
        else:
            return None