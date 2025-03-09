from collections import Counter
from src.products import Product

class Cart:

	def __init__(self):
		self.items = []

	def addProducts(self, Product):
		self.items.append(Product)

	def PrecioTotal(self):

		product_counts = Counter([p.code for p in self.items])
		total = 0

		product_prices = {
			"GR1": 3.11,
			"SR1": 5.00,
			"CF1": 11.23
		}

		for productCode, quantity in product_counts.items():
			if productCode == "GR1":
				total += (quantity // 2 + quantity % 2) * product_prices['GR1']
			elif productCode == "SR1" and quantity >= 3:
				total += quantity * 4.50
			elif productCode == "CF1" and quantity >= 3:
				total += quantity * (product_prices['CF1'] * 2 / 3)
			else:
				total += quantity * product_prices.get(productCode, 0)

		return round(total, 2)
