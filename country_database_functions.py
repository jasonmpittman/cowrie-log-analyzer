import pathlib
import sqlite3
from sqlite3 import Error

country_db = "country_lookup.db"

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

def query_country_db(ip):
	sql = f"SELECT country_name FROM ip_lookup WHERE {ip} >= ip_from and {ip} < ip_to"
	conn = create_connection(country_db)
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(sql)
		country = c.fetchall()
		c.close()
		return country[0][0]
	except Error as e:
		print(e)

def run_sql(sql):
	conn = create_connection(country_db)
	try:
		c = conn.cursor()
		c.execute(sql)
		c.close()
		conn.commit()
	except Error as e:
		print(e)

def strip():
	sql = """UPDATE ip_lookup SET country_name = REPLACE(country_name, '\n', '') """
	run_sql(sql)
	print("strip ran")

def ip_to_decimal(ip):
	ip_parts = ip.split(".")
	return int(ip_parts[0]) * 256**3 + int(ip_parts[1]) * 256**2 + int(ip_parts[2]) * 256**1 + int(ip_parts[3])

def get_ip_country(ip):
	ip_dec = ip_to_decimal(ip)
	country = query_country_db(ip_dec)
	country = str(country)
	return country

#
