import os
import yaml
import logging

from scrapper.api_scrapper import ApiScrapper 
from config.constants import BaseURL, CatalogURL
from config.endpoints import ApiEndpoints
from utils.logger import setup_logger
from scripts.get_hub_details import HubsDetailsScrapper

setup_logger("logs/scrape1.log")
logger = logging.getLogger(__name__)

def load_config(config_path="config/quotation.yaml"):
	base_dir = os.path.dirname(os.path.abspath(__file__))
	config_path = os.path.join(base_dir, config_path)
	with open(config_path, "r") as f:
		return yaml.safe_load(f)

def create_scrapper_obj(config):
	if config.get('scrapper') == 'api':
		return ApiScrapper(config)
	else:
		# return SeleniumScrapper(config)
		pass

def main():
	os.makedirs("output", exist_ok=True)
	os.makedirs("logs", exist_ok=True)

	
	quotations = load_config()

	quote = quotations.get('buyers_requirements')[0]
	scrapper_obj = create_scrapper_obj(quote)
	endpoints = ApiEndpoints()
	# url1 = f"{BaseURL}{endpoints.format(endpoints.make_city, make='kia',city='jaipur')}"
	# print(url1)

	# To get the current count of available cars by cities
	"""
	url = f"{CatalogURL}{endpoints.catalog_city}"
	logger.info(f"Running fetch for URL : {url}")
	data = scrapper_obj.fetch(url)
	json_data = data.json()
	for city in json_data:
		logger.info(f"{city['cityName']} have total {city['count']} used cars available currently.")
	"""
	hub_obj = HubsDetailsScrapper(scrapper_obj, endpoints)
	data = hub_obj.get_all_hubs()
	hub_obj.generate_csv('hub_details_1.csv', ['City ID', 'Branch', 'PinCode', 'Available Cars'], data)
	

if __name__ == "__main__":
	main()