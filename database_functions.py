import pathlib
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	""" create a database connection to a SQLite database """
	conn = None

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
		return conn

def create_table(conn):
	create_table_sql = r"CREATE TABLE IF NOT EXISTS ip_lookup (ip_from integer, ip_to integer, country_code text, country_name text);"
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(create_table_sql)
		c.close()
	except Error as e:
		print(e)



def insert_country(conn, country_info):
	sql = r"INSERT INTO ip_lookup(ip_from, ip_to, country_code, country_name) VALUES(?,?,?,?)"
	cur = conn.cursor()
	cur.execute(sql, country_info)
	cur.close()

def populate_country_lookup(conn):
	filename = "IP2LOCATION-LITE-DB1.CSV"
	with open(filename, "r") as file:
		for line in file:
			split_line = line.split(",")
			insert_country(conn, (int(split_line[0].strip('"')), int(split_line[1].strip('"')), split_line[2].strip('"'), split_line[3].strip('"')))

	conn.commit()
