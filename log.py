import logging

class Logger:
	def __init__(self, name):
		#"%(levelname)s:%(name)s:%(message)s"
		self.logger = logging.getLogger(name)
		self.logger.setLevel(logging.INFO)
		self.file_handler = logging.FileHandler("logfile.log")
		self.formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
		self.file_handler.setFormatter(self.formatter)
		self.logger.addHandler(self.file_handler)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)
