import mysql.connector


def connect():

    return mysql.connector.connect(

        host="localhost",

        user="root",

        password="YOUR_PASSWORD",

        database="parksense_ai",

        auth_plugin="mysql_native_password"

    )
