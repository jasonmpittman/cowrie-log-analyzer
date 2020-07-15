import pathlib
import sqlite3
from sqlite3 import Error

import log

country_db_logger = log.Logger("country_db")

country_db = "country_lookup.db"
'''
Create a database connection to a SQLite database
Input: Database file name
Output: a connection to the database
'''
def create_connection(db_file):

	conn = None
	try:
		conn = sqlite3.connect(db_file)
		country_db_logger.info("", create_connection.__name__, f"Successfully connected to {db_file}")
		return conn
	except Error as e:
		print(e)
		country_db_logger.info("", create_connection.__name__, f"Failed to connect to {db_file}")
		return conn

'''
Creates a table called ip_lookup with ip_from, ip_to, country_code, country_name as columns
Input: Takes a connection as input
'''
def create_table(conn):
	create_table_sql = r"CREATE TABLE IF NOT EXISTS ip_lookup (ip_from integer, ip_to integer, country_code text, country_name text);"
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(create_table_sql)
		c.close()
	except Error as e:
		print(e)
'''
Inserts a row into the database
Input: a connection, the information about the row as a touple
'''
def insert_country(conn, country_info):
	sql = r"INSERT INTO ip_lookup(ip_from, ip_to, country_code, country_name) VALUES(?,?,?,?)"
	cur = conn.cursor()
	cur.execute(sql, country_info)
	cur.close()

'''
Takes a connection and populates the database with ip location data from the csv file

This site or product includes IP2Location LITE data available from http://www.ip2location.com.
Input: Connection
'''
def populate_country_lookup(conn):
	filename = "IP2LOCATION-LITE-DB1.CSV"
	with open(filename, "r") as file:
		for line in file:
			split_line = line.split(",")
			insert_country(conn, (int(split_line[0].strip('"')), int(split_line[1].strip('"')), split_line[2].strip('"'), split_line[3].strip('"')))

	conn.commit()

'''
Searches for the country based on the ip range
Input: ip (in decimal format)
Output: String with the country name
'''
def query_country_db(ip):
	sql = f"SELECT country_name FROM ip_lookup WHERE {ip} >= ip_from and {ip} < ip_to"
	conn = create_connection(country_db)
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(sql)
		country = c.fetchall()
		c.close()
		country_db_logger.info("", query_country_db.__name__, f"Successfully found ip: {ip}")
		return country[0][0]
	except Error as e:
		country_db_logger.info("", query_country_db.__name__, f"failed to find ip: {ip}")
		print(e)

'''
Runs sql provided
Input: sql
'''
def run_sql(sql):
	conn = create_connection(country_db)
	try:
		c = conn.cursor()
		c.execute(sql)
		c.close()
		conn.commit()
	except Error as e:
		print(e)
'''
Strips newline character from coutry names
'''
def strip():
	sql = """UPDATE ip_lookup SET country_name = REPLACE(country_name, '\n', '') """
	run_sql(sql)

'''
Takes an ip address as a string and converts it to decimal format
Input: ip (as a string)
Output: ip (in decimal format)
'''
def ip_to_decimal(ip):
	ip_parts = ip.split(".")
	return int(ip_parts[0]) * 256**3 + int(ip_parts[1]) * 256**2 + int(ip_parts[2]) * 256**1 + int(ip_parts[3])

'''
Takes in an ip address and returns the country
Input: ip (string)
Output: country name (string)
'''
def get_ip_country(ip):
	ip_dec = ip_to_decimal(ip)
	country = query_country_db(ip_dec)
	country = str(country)
	return country

#
