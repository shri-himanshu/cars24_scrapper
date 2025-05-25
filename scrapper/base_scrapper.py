"""
This file defines a base scrapper class.
Other interface specific scrappers should follow the same structre and method namings for consistency
"""

from abc import ABC, abstractmethod
import logging

class BaseScrapper(ABC):

	def __init__(self, config):
		self.name = config.get("name")
		self.config = config
		self.logger = logging.getLogger(self.name)


	@abstractmethod
	def fetch(self, **kwargs):
		"""Fetch page content"""
		pass

	@abstractmethod
	def parse(self, content, **kwargs):
		"""Parse the raw content fetched"""
		pass

	@abstractmethod
	def save(self, data, output_path, **kwargs):
		"""Save teh extracted data to a CSV"""
		import pandas as pd 
		df = pd.DataFrame(data)
		df.to_csv(output_path, index=False)
		self.logger.info(f"Saving the data for {self.name} to {output_path}")