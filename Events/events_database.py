#!/usr/bin/env python3

__author__ = "Kevin A. Rubin, Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Kevin A. Rubin, Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Release"
__dependecies__ = "sqlite3, json, datetime, country_database, log"

import sqlite3

from sqlite3 import Error

import json

import datetime

from Events import country_database

from Log import log

events_db_log = log.Logger("events_db")


def create_connection(db_file="Events/events.db"):
	"""
	Creates a database connection to a SQLite database (specifically used for events.db)

	Parameters
	----------
	db_file : str
	"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		create_table(conn)
		create_command_table(conn)
		events_db_log.info("", create_connection.__name__, f"Successfully connected to {db_file}")
		return conn
	except Error as e:
		print(e)
		events_db_log.info("", create_connection.__name__, f"Failed to connect to {db_file}")
		return conn



'''

'''
def create_command_table(conn):
	"""
	Creates the command table if it does not exist

	Parameters
	----------
	conn : database connection structure
	"""
	create_command_sql = """CREATE TABLE IF NOT EXISTS commands (
						foreign_key INTEGER,
						command TEXT);
						"""
	run_sql(conn, create_command_sql)

def run_sql(conn, sql):
	"""
	Input: conn --> connection, sql --> sql query
	Output: res --> results of the query

	Parameters
	----------
	conn : database connection structure
	sql : str
	"""
	try:
		c = conn.cursor()
		#executes the phrase
		c.execute(sql)
		res = c.fetchall()
		c.close()
		conn.commit()
		return res
	except Error as e:
		print(e)

def create_table(conn):
	"""
	Creates the events table if it does not already exist
	Input: conn --> a connection

	Parameters
	----------
	conn : database connection structure
	"""
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

	run_sql(conn, create_table_sql)


def get_config():
	"""
	Loads the configuration file (json) into a python dictionary
	Output: config_dict --> a dictionary
	"""
	with open("config/types.config.json", "r") as config_file:
  		config = config_file.read()
	config_dict = json.loads(config)
	return config_dict


def get_type(event_id):
	"""
	Uses the configuration dictionary to categorize the type of event
	Input: event_id
	Outputs: categorization

	Parameters
	----------
	event_id : str
	"""
	config_dict = get_config()
	try:
		return config_dict[event_id]
	except:
		print(f"Missing from config file: {event_id}, full event id will be used")
		events_db_log.info("", get_type.__name__, f"Missing from config file: {event_id}, full event id will be used")
		return event_id


def get_file_name(file_path):
	"""
	Takes in a file_path and gets the actual file name from the path
	Input: file path
	Output: file name

	Parameters
	----------
	file_path : str
	"""
	if file_path == "-":
		return "-"
	path = file_path.split("/")
	return path[-1]


def get_data_touple(event):
	"""
	Takes in an event and prepares the data before returning it as a touple for sql
	Input: event
	Output: touple of all event information

	Parameters
	----------
	event : event object
	"""
	type = get_type(event.event["eventid"])
	ip = event.get("src_ip")
	username = event.get("username")
	password = event.get("password")
	filename = get_file_name(event.get("url"))
	country = country_database.get_ip_country(event.get("src_ip"))

	duration = event.get("duration")
	if duration != "-":
		duration = float(duration)

	timestamp = event.get("timestamp")

	dt_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
	date_time = str(dt_obj)
	message = event.get("message")
	return (type, ip, username, password, filename, country, duration, date_time, message)

def get_command_list(command_line):
	"""
	Splits a line of commands into their compenents
	Input: command_line -> a line with commands
	Output: command_line -> list of commands

	Parameters
	----------
	command_line : str
	"""
	command_line = command_line.replace("CMD: ", "")
	command_line = command_line.split("; ")
	return command_line


def add_event(conn, event):
	"""
	Inserts and event into the events database
	Input: conn, event
	Output: rowid -> unique row identifier

	Parameters
	----------
	conn : database connection
	event : event object
	"""

	sql = """INSERT INTO events(type, ip_address, username, password, filename, country, duration, timestamp, message) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)  """
	preped_data = get_data_touple(event)
	cur = conn.cursor()
	type, _, _, _, _, _, _, _, message = preped_data
	rowid = 0

	try:
		cur.execute(sql, preped_data)

		rowid = cur.lastrowid

	except:
		events_db_log.info("", add_event.__name__, f"Nothing was inserted")
		return False

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
				events_db_log.info("", add_event.__name__, f"Command inserted")
			except:
				print("Failed to insert command")
				events_db_log.info("", add_event.__name__, f"Failed to insert command")
				return False
	return True

def query_top_ten(conn, col):
	"""
	Returns a string that lists the top 10 most frequent data for a given column and the #1 (these are returned as a touple)
	Input: conn, col --> a column name to run top 10 on
	Output: (strReturn -> top 10 string, first -> #1)

	Parameters
	----------
	conn : database connection structure
	col : str
	"""
	sql = f"""SELECT {col},COUNT({col}) AS cnt FROM events
			WHERE {col} NOT IN ('-')
			GROUP BY {col}
			ORDER BY cnt DESC;"""

	cur = conn.cursor()

	try:
		i = 0
		cur.execute(sql)
		res = cur.fetchall()

		strReturn = ""
		stop_val = 10
		print_num = 1
		events_db_log.info("", query_top_ten.__name__, f"Top ten queried {col}")
		while i < stop_val and i < len(res):
			key, _ = res[i]

			if print_num == 10:
				strReturn += str(print_num) + ". " + str(key) + "\n"
			else:
				strReturn += str(print_num) + ".  " + str(key) + "\n"
			print_num += 1

			i += 1
		first, _ = res[0]
		cur.close()
		events_db_log.info("", query_top_ten.__name__, f"Top ten queried {col} - Successful")
		return (strReturn, first)
	except:
		print(f"Failed {col}")
		return None


def top_ten_user_pass(conn):
	"""
	A special function that does the same as the other top ten but customized for username and password pair
	Input: conn
	Output: strReturn -> top 10 string, first -> #1

	Parameters
	----------
	conn : database connection structure
	"""
	sql = f"""SELECT username, password FROM events WHERE username NOT IN ('-') and password NOT IN ('-');"""
	cur = conn.cursor()
	i = 0
	cur.execute(sql)
	res = cur.fetchall()

	strReturn = ""
	totals = {}

	for pair in res:
		usr, p = pair
		combined = usr + ": " + p
		if combined not in totals:
			totals.update({combined : 1})
		else:
			totals[combined] += 1

	sortedDictionary = sorted(totals.items(), key = lambda x : x[1], reverse=True)
	events_db_log.info("", top_ten_user_pass.__name__, f"Top ten queried user_pass - Successful")
	while i < 10 and i < len(sortedDictionary):
		key, value = sortedDictionary[i]
		if i == 9:
			strReturn += str(i + 1) + ". " + str(key) + "\n"
		else:
			strReturn += str(i + 1) + ".  " + str(key) + "\n"
		i += 1
	first, val = sortedDictionary[0]
	return strReturn, first


def longest_durations():
	"""
	Gets the top 10 and #1 longest duration (not by frequency)
	Output: (output_str -> top 10 string, first -> #1)
	"""
	output_str = ""
	sql = """SELECT duration FROM events
			WHERE duration NOT IN ('-')
			ORDER BY duration DESC;"""
	conn = create_connection()
	res = run_sql(conn, sql)
	i = 0
	first, = res[0]
	while i < 10 and i < len(res):
		val, = res[i]
		val = round(val, 5)
		if i == 9:
			output_str = output_str + f"{i+1}. {val}"
		else:
			output_str = output_str + f"{i+1}.  {val}\n"
		i += 1
	events_db_log.info("", longest_durations.__name__, f"Top ten longest durations - Successful")
	return output_str, first
