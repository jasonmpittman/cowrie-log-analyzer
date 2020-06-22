import sqlite3

from sqlite3 import Error

import json

from country_database import *

import datetime

from event_class import *

'''Creates a database connection to a SQLite database '''
def create_connection(db_file="events.db"):

	conn = None

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
		return conn

'''
Creates the command table
'''

def create_command_table(conn):
	create_command_sql = """CREATE TABLE IF NOT EXISTS commands (
						foreign_key INTEGER,
						command TEXT);
						"""
	run_sql(conn, create_command_sql)

'''
Input: conn --> connection, sql --> sql query
Output: res --> results of the query
'''

def run_sql(conn, sql):
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

'''
Creates the events table
Input: conn --> a connection
'''
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

	run_sql(conn, create_table_sql)
'''
Loads the configuration file (json) into a python dictionary
Output: config_dict --> a dictionary
'''
def get_config():
	with open('types.config.json', 'r') as config_file:
  		config = config_file.read()
	config_dict = json.loads(config)
	return config_dict

'''
Uses the configuration dictionary to categorize the type of event
Input: event_id
Outputs: categorization
'''
def get_type(event_id):
	config_dict = get_config()
	try:
		return config_dict[event_id]
	except:
		print(f"Missing from config file: {event_id}, full event id will be used")
		return event_id

'''
Takes in a file_path and gets the actual file name from the path
Input: file path
Output: file name
'''
def get_file_name(file_path):
	if file_path == "-":
		return "-"
	path = file_path.split("/")
	return path[-1]

'''
Takes in an event and prepares the data before returning it as a touple for sql
Input: event
Output: touple of information
'''
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

'''
Splits a line of commands into their compenents
Input: command_line -> a line with commands
Output: command_line -> list of commands
'''
def get_command_list(command_line):
	command_line = command_line.replace("CMD: ", "")
	command_line = command_line.split("; ")
	return command_line

'''
Inserts and event into the events database
Input: conn, event
Output: rowid -> unique row identifier
'''
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
			except:
				print("Failed to insert command")
				return None
	return rowid

'''
Returns a string that lists the top 10 most frequent data for a given column and the #1 (these are returned as a touple)
Input: conn, col1 --> a column name to run top 10 on
Output: (strReturn -> top 10 string, first -> #1)
'''
def query_top_ten(conn, col1):
	sql = f"""SELECT {col1},COUNT({col1}) AS cnt FROM events
			WHERE {col1} NOT IN ('-')
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

			if print_num == 10:
				strReturn += str(print_num) + ". " + str(key) + "\n"
			else:
				strReturn += str(print_num) + ".  " + str(key) + "\n"
			print_num += 1

			i += 1
		first, _ = res[0]
		cur.close()
		return (strReturn, first)
	except:
		print("Failed")
		return None

'''
A special function that does the same as the other top ten but customized for username and password pair
Input: conn
Output: strReturn -> top 10 string, first -> #1
'''
def top_ten_user_pass(conn):
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

	while i < 10 and i < len(sortedDictionary):
		key, value = sortedDictionary[i]
		if i == 9:
			strReturn += str(i + 1) + ". " + str(key) + "\n"
		else:
			strReturn += str(i + 1) + ".  " + str(key) + "\n"
		i += 1
	first, val = sortedDictionary[0]
	return strReturn, first

'''
Gets the top 10 and #1 longest duration (not by frequency)
Output: (output_str -> top 10 string, first -> #1)
'''
def longest_durations():
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
		if i == 9:
			output_str = output_str + f"{i+1}. {val}"
		else:
			output_str = output_str + f"{i+1}.  {val}\n"
		i += 1
	return output_str, first

# conn = create_connection()
# create_table(conn)
# conn.commit()
# create_command_table(conn)
# conn.commit()
