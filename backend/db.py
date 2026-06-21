import mysql.connector


def connect():

    return mysql.connector.connect(

        host="localhost",

        user="root",

        password="R7x$91kZ@fL#eB2p!",

        database="parksense_ai",

        auth_plugin="mysql_native_password"

    )