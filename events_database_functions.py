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
						message TEXT,
						constraint event_unique unique(type, ip_address, username, password, country, duration, timestamp, message)
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
	date_time = dt_obj
	message = event.Get("message")
	return (type, ip, username, password, filename, country, duration, date_time, message)


def add_event(conn, event):
	sql = """INSERT INTO events(type, ip_address, username, password, filename, country, duration, timestamp, message) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)  """
	preped_data = get_data_touple(event)
	cur = conn.cursor()

	try:
		cur.execute(sql, preped_data)
		return cur.lastrowid
	except:
		return None

def query_top_ten(conn, col):
	sql = f"""SELECT {col},COUNT({col}) AS cnt FROM events
			GROUP BY {col}
			ORDER BY cnt DESC;"""
	cur = conn.cursor()

	try:
		i = 0
		cur.execute(sql)
		res = cur.fetchall()

		strReturn = ""
		while i < 10 and i < len(res):
			key, _ = res[i]
			if i == 9:
				strReturn += str(i+1) + ". " + str(key) + "\n"
			else:
				strReturn += str(i+1) + ".  " + str(key) + "\n"
			i += 1
		first, _ = res[0]
		return strReturn, first
	except:
		return None
