from events_class import *
from events_database import *
import sys

class logic:
	def __init__(self):
		self.events_object = Events()

	def get_data(self, name):
		print("system")
		self.events_object.get_data(name)
		return True

	def update_database(self):
		conn = create_connection("events.db")
		config_dict = get_config()
		for event in self.events_object.events:
			add_event(conn, event)

		conn.commit()
		conn = create_connection("events.db")

		# self.update_screen()

	# '''
	# update_screen --> updates all the visible data with what is in the datebase
	# '''
	# def update_screen(self):
	# 	conn = create_connection("events.db")
	# 	try:
	# 		ip_res, ip1 = query_top_ten(conn, "ip_address")
	# 		self.ip_address.Clear()
	# 		self.ip_address.Append(ip_res)
	#
	# 		usr_res, usr1 = query_top_ten(conn, "username")
	# 		self.user_names.Clear()
	# 		self.user_names.Append(usr_res)
	#
	# 		pass_res, pass1 = query_top_ten(conn, "password")
	# 		self.passwords.Clear()
	# 		self.passwords.Append(pass_res)
	#
	# 		user_pass_res, usr_pass_1 = top_ten_user_pass(conn)
	# 		self.user_and_pass.Clear()
	# 		self.user_and_pass.Append(user_pass_res)
	#
	# 		#more information needed
	# 		download_res, download1 = query_top_ten(conn, "filename")
	# 		self.download_file.Clear()
	# 		self.download_file.Append(download_res)
	#
	# 		country_res, country1 = query_top_ten(conn, "country")
	# 		self.origin_country.Clear()
	# 		self.origin_country.Append(country_res)
	#
	# 		sess_res, sess1 = longest_durations()
	# 		self.session_duration.Clear()
	# 		self.session_duration.Append(sess_res)
	#
	# 		self.overall_one.Clear()
	# 		self.overall_one.Append(f"- ip: {ip1}\n- usr: {usr1}\n- pass: {pass1}\n- User/Pass: {usr_pass_1} \n- Downloads: {download1}\n- Country: {country1}\n- Duration: {sess1}")
	# 	except:
	# 		print("Please Import Data")


	def no_update(self):
		pass

	def exit(self):
		sys.exit()
