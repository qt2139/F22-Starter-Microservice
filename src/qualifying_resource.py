import pymysql
import os

class F1:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get('DBUSER')
        pw = os.environ.get('DBPW')
        host = os.environ.get('DBHOST')

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=host,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_qualifying():

        sql = "SELECT * FROM f22_databases.qualify";
        conn = F1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def append_new_qualifying(qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3):
        sql = "INSERT INTO f22_databases.qualify VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        conn = F1._get_connection()
        cur = conn.cursor()
        try:
            conn.begin()
            res = cur.execute(sql, (qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            return e

    @staticmethod
    def delete_qualifying(id):
        sql = "DELETE from f22_databases.qualify where circuitId = %s;"
        conn = F1._get_connection()
        cur = conn.cursor()
        try:
            conn.begin()
            res = cur.execute(sql, (id))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            return e

    @staticmethod
    def update_qualifying(name, value):
        sql = "UPDATE f22_databases.qualify set driverId = %s where circuitId = %s;"
        conn = F1._get_connection()
        cur = conn.cursor()
        try:
            conn.begin()
            res = cur.execute(sql, (value, name))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            return e
