import psycopg2
class Model:
    
    def executeUpdateSQL(self, sql):
        conn = psycopg2.connect("dbname=E-shop user=postgres password=ADMIN")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def executeFetchSQL(sql):
        conn = psycopg2.connect("dbname=E-shop user=postgres password=ADMIN")
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result