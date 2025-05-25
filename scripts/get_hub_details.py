import os
import yaml
import logging
import csv

from scrapper.api_scrapper import ApiScrapper 
from config.constants import BaseURL, CatalogURL
from config.endpoints import ApiEndpoints
from utils.logger import setup_logger

setup_logger("logs/scrape1.log")
logger = logging.getLogger(__name__)


class HubsDetailsScrapper:

	def __init__(self, scrapper_obj, endpoints):
		self.scrapper_obj = scrapper_obj
		self.endpoints = endpoints

	def get_all_hubs(self):
		city_id_dict = {}
		city_ids = []
		catalog_url = f"{CatalogURL}{self.endpoints.catalog_city}"
		logger.info(f"Running fetch for URL : {catalog_url}")
		city_data = self.scrapper_obj.fetch(catalog_url)
		city_json = city_data.json()
		# To get mapping of city name to id
		for city in city_json:
			city_id_dict[city['cityName']] = city['cityId']
			city_ids.append(city['cityId'])
		hub_details = []
		for city in city_ids[:5]:
			hub_url =  f"{CatalogURL}{self.endpoints.format(self.endpoints.hubs, cityId=city)}"
			#logger.info(f"Running fetch for URL : {hub_url}")
			hub_data = self.scrapper_obj.fetch(hub_url)
			hub_json = hub_data.json()
			#print(hub_json)
			for hub in hub_json:
				#logger.info(f"{hub['name']} hub is at pincode {hub['pincode']} is managed by {hub['salesManager']['name']}")
				# hub_details.append
				hub_details.append(hub)

		return hub_details

	def generate_csv(self, file_path, columns, data):
		with open(file_path, mode='w',  newline='', encoding='utf-8') as f:
			writer = csv.writer(f)
			writer.writerow(columns)
			import pdb;pdb.set_trace()
			for hub in data:
				city_id = hub.get('legacyId')
				name = hub.get('name')
				pin = hub.get('pincode')
				available_cars = hub.get('count')

				writer.writerow([city_id, name, pin, available_cars])
			print('CSV file created')
