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

def get_command_list(command_line):
	command_line = command_line.replace("CMD: ", "")
	command_line = command_line.split("; ")
	return command_line

def add_event(conn, event):
	sql = """INSERT INTO events(type, ip_address, username, password, filename, country, duration, timestamp, message) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)  """
	preped_data = get_data_touple(event)
	cur = conn.cursor()
	type, _, _, _, _, _, _, _, message = preped_data
	rowid = 0

	try:
		cur.execute(sql, preped_data)
		# print(cur.lastrowid)
		rowid = cur.lastrowid
	except:
		print("nothing was inserted")
		return None

	if type == "Command":
		foreign_key = cur.lastrowid
		cur.close()
		commands_list = get_command_list(message)
		sql = """INSERT INTO commands(foreign_key, command) VALUES(?, ?)"""
		cur = conn.cursor()
		for com in commands_list:
			data = (foreign_key, com)
			try:
				cur.execute(sql, data)
				rowid = cur.lastrowid
			except:
				print("Failed to insert command")
				return None
	return rowid


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
		stop_val = 10
		print_num = 1
		while i < stop_val and i < len(res):
			key, _ = res[i]
			if key != "-":
				if print_num == 10:
					strReturn += str(print_num) + ". " + str(key) + "\n"
				else:
					strReturn += str(print_num) + ".  " + str(key) + "\n"
				print_num += 1
			else:
				stop_val += 1
			i += 1
		first, _ = res[0]
		if first == "-":
			first = res[1]
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
		if usr != "-" and p != "-":
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

# conn = create_connection()
# create_table(conn)
# conn.commit()
# create_command_table(conn)
# conn.commit()
