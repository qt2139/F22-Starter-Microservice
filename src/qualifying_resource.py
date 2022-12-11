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
            user="root",
            password="dbuserdbuser",
            host="localhost",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_qualifying(id):

        sql = "SELECT * FROM f22_databases.qualify where qualifyId = %s" % (id);
        conn = F1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def append_new_qualifying(data):

        sql = "INSERT INTO f22_databases.qualify VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)";
        conn = F1._get_connection()
        cur = conn.cursor()
        try:
            conn.begin()
            res = cur.execute(sql, (data['qualifyId'],data['raceId'],data['driverId'],data['constructorId'],data['number'],data['position'],data['q1'],data['q2'],data['q3']))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            return e

    @staticmethod
    def delete_qualifying(id):
        sql = "DELETE FROM f22_databases.qualify where qualifyId = %s";
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
        sql = "UPDATE f22_databases.qualify set driverId = %s where qualifyId = %s;"
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
