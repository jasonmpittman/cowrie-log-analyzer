import sqlite3

from sqlite3 import Error

import json

from country_database_functions import *

import datetime

from event_class import *

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
	country = get_ip_country(event.Get("src_ip"))

	duration = event.Get("duration")
	if duration != None:
		duration = float(duration)

	timestamp = event.Get("timestamp")

	dt_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
	date_time = f"datetime({dt_obj})"
	message = event.Get("message")
	return (type, ip, username, password, filename, country, duration, date_time, message)


def add_event(data):
	pass

conn = create_connection(events_db)
get_file_name("http://45.148.10.95/dlrdlrdlrdlr00001/d4mnasdasd4mn.x86")

E = Event({"eventid":"cowrie.session.connect","src_ip":"193.142.146.21","src_port":43854,"timestamp":"2020-03-19T00:44:31.639222Z","message":"New connection: 193.142.146.21:43854 (10.1.1.3:2222) [session: cafb43d1579d]","dst_ip":"10.1.1.3","protocol":"ssh","session":"cafb43d1579d","dst_port":2222,"sensor":"svrvmcw"})
print(get_data_touple(E))
