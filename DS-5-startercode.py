import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly. #COMPLETE THE FOLLOWING BELOW
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse
	def add_item(self, item):
		self.items.append(item) 

	# Returns the item in the warehouse with the lowest stock
	def get_min_stock(self):
		min_stock = self.items[0].stock
		min_item = self.items[0]
		for item in self.items:
			if min_stock >= item.stock:
				min_item = item
				min_stock = item.stock
		return min_item


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = self.items[0].price
		max_item = self.items[0]
		for item in self.items:
			if max_price <= item.price:
				max_item = item
				max_price = item.price
		return max_item


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertTrue(count_a("aaa")==3)

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		warehouse = Warehouse()
		warehouse.add_item(self.item1)
		warehouse.add_item(self.item2)
		warehouse.add_item(self.item3)
		warehouse.add_item(self.item4)
		warehouse.add_item(self.item5)


	## Check to see whether warehouse correctly returns the item with the lowest stock -
	def test_warehouse_min_stocks(self):
		warehouse = Warehouse(items = [self.item1,self.item2,self.item3,self.item4,self.item5])
		self.assertEqual(warehouse.get_min_stock(), self.item1)


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		warehouse = Warehouse(items = [self.item1,self.item2,self.item3,self.item4,self.item5])
		self.assertEqual(warehouse.get_max_price(), self.item1)
		

def main():
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()