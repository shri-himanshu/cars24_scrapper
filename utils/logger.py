# utility function for setting up logger settings


import logging

def setup_logger(log_file):
	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s %(levelname)s [%(name)s]: %(message)s",
		handlers=[logging.FileHandler(log_file),
			logging.StreamHandler()]
		)