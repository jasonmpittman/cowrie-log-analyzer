import sqlite3

from sqlite3 import Error

import json

from country_database import *

import datetime

from event_class import *


def create_connection(db_file="events.db"):
	""" create a database connection to a SQLite database """
	conn = None

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
		return conn

def create_command_table(conn):
	create_command_sql = """CREATE TABLE IF NOT EXISTS commands (
						foreign_key INTEGER,
						command TEXT);
						"""
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(create_command_sql)
		c.close()
		conn.commit()
	except Error as e:
		print(e)


#create unique index unq_notify_users_2 on notify_users(language_code, username);
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
						constraint event_unique unique(type, ip_address, username, password, filename, country, duration, timestamp, message)
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

unknown_res = "[]"

def get_file_name(file_path):
	if file_path == "-":
		return "-"
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
	if duration != "-":
		duration = float(duration)

	timestamp = event.Get("timestamp")

	dt_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
	date_time = str(dt_obj)
	message = event.Get("message")
	return (type, ip, username, password, filename, country, duration, date_time, message)


def add_event(conn, event):
	sql = """INSERT INTO events(type, ip_address, username, password, filename, country, duration, timestamp, message) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)  """
	preped_data = get_data_touple(event)
	cur = conn.cursor()

	try:
		cur.execute(sql, preped_data)
		print(cur.lastrowid)
		return cur.lastrowid
	except:
		print("nothing was inserted")
		return None

def query_top_ten(conn, col1):
	sql = f"""SELECT {col1},COUNT({col1}) AS cnt FROM events
			GROUP BY {col1}
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
		cur.close()
		return (strReturn, first)
	except:
		print("Failed")
		return None

def top_ten_user_pass(conn):
	sql = f"""SELECT username, password FROM events;"""
	cur = conn.cursor()
	i = 0
	cur.execute(sql)
	res = cur.fetchall()

	strReturn = ""
	totals = {}

	for pair in res:
		usr, p = pair
		if usr != None and p != None:
			combined = usr + ": " + p
			if combined not in totals:
				totals.update({combined : 1})
			else:
				totals[combined] += 1

	sortedDictionary = sorted(totals.items(), key = lambda x : x[1], reverse=True)

	while i < 10 and i < len(sortedDictionary):
		key, value = sortedDictionary[i]
		if i == 9:
			strReturn += str(i + 1) + ". " + str(key) + "\n"
		else:
			strReturn += str(i + 1) + ".  " + str(key) + "\n"
		i += 1
	first, val = sortedDictionary[0]
	return strReturn, first

conn = create_connection()
create_table(conn)
