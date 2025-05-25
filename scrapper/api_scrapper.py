"""
This file defines the methods to scrape the data from API interface
"""
import requests
import json
from .base_scrapper import BaseScrapper


class ApiScrapper(BaseScrapper):

	def fetch(self, url):
		try:
			raw_response = requests.get(url)
			self.logger.info(f"Fetched data from URL : {url}")
			return raw_response
		except requests.RequestException as err:
			self.logger.info(f"Failed to fetch data from {url}. ERROR : {err}")
			return None

	def parse(self):
		pass

	def save(self):
		pass