"""
This file stores all the required api endpoints for the site
"""


class ApiEndpoints:
	# make_model_city = "buy-used-{make}-{model}-cars-{city}/"
	make_city = "buy-used-{make}-cars-{city}"
	# fuel_city = "buy-used-{fuel}-cars-{city}"
	# type_city = "buy-used-{types}-cars-{city}"  # eg : buy-used-sedan-cars-jaipur/
	# budget_city = "buy-used-cars-under-{budget_in_lakh}-lakhs-{city}/"  #  buy-used-cars-under-20-lakhs-jaipur/


	# endpoints for catalog URL
	catalog_city = "website/v1/cities"
	hubs = "hub/v1/{cityId}"


	@staticmethod
	def format(endpoint_template, **kwargs):
		return endpoint_template.format(**kwargs)
