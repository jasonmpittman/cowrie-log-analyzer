import sqlite3

from sqlite3 import Error

import json

events_db = "events.db"

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
	create_table_sql = """CREATE TABLE IF NOT EXISTS events (
						type TEXT,
						ip_address TEXT,
						username TEXT,
						password TEXT,
						filename TEXT,
						country TEXT,
						duration REAL,
						timestamp TEXT,
						message TEXT
						);"""
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(create_table_sql)
		c.close()
		conn.commit()
	except Error as e:
		print(e)

def get_config():
	with open('types.config.json', 'r') as config_file:
  		config = config_file.read()
	config_dict = json.loads(config)
	return config_dict

def get_type(event_id):
	config_dict = get_config()
	try:
		return config_dict[event_id]
	except:
		print(f"Missing from config file: {event_id}, full event id will be used")
		return event_id

def get_file_name(file_path):
	if file_path == None:
		return None
	path = file_path.split("/")
	return path[-1]

def get_data_touple(event):
	type = get_type(event.event["eventid"])
	ip = event.Get("src_ip")
	username = event.Get("username")
	password = event.Get("password")
	filename = get_file_name(event.Get("url"))
	# country =


def add_event(data):
	pass

conn = create_connection(events_db)
get_file_name("http://45.148.10.95/dlrdlrdlrdlr00001/d4mnasdasd4mn.x86")
