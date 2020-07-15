import logging

class Logger:
	def __init__(self, name):
		#"%(levelname)s:%(name)s:%(message)s"
		self.logger = logging.getLogger(name)
		self.logger.setLevel(logging.INFO)
		self.file_handler = logging.FileHandler("logfile.log")
		self.formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s:%(message)s")
		self.file_handler.setFormatter(self.formatter)
		self.logger.addHandler(self.file_handler)

	def info(self, class_name, function_name, message):
		if class_name == "":
			self.logger.info(f"{function_name} - {message}")
		else:
			self.logger.info(f"{class_name}.{function_name} - {message}")

	def warning(self, class_name, function_name, message):
		if class_name == "":
			self.logger.warning(f"{function_name} - {message}")
		else:
			self.logger.warning(f"{class_name}.{function_name} - {message}")

	def error(self, message):
		self.logger.error(message)
