class HotBeverage:
	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"
	def description(self):
		return "Just some hot water in a cup."
	def __str__(self) -> str:
		TEMEPLATE = ("name : {name}\n"
					"price: {price:0.2f}\n"
					"description: {description}")
		return TEMEPLATE.format(name=self.name, price=self.price, description=self.description())

class Tea(HotBeverage):
	def __init__(self):
		self.price = 0.30
		self.name = "tea"
	def description(self):
		return "Just some hot water in a cup."

class Coffee(HotBeverage):
	def __init__(self):
		self.price = 0.40
		self.name = "coffee"
	def description(self):
		return "A coffee, to stay awake."

class Cappuccino(HotBeverage):
	def __init__(self):
		self.price = 0.45
		self.name = "cappuccino"
	def description(self):
		return "Un po' di Italia nella sua tazza!"

class Chocolate(HotBeverage):
	def __init__(self):
		self.price = 0.50
		self.name = "chocolate"
	def description(self):
		return "Chocolate, sweet chocolate..."

def main():
	print(HotBeverage(), '\n')
	print(Tea(), '\n')
	print(Coffee(), '\n')
	print(Cappuccino(), '\n')
	print(Chocolate(), '\n')

if __name__ == "__main__":
	main()
