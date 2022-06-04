from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate
import random

class CoffeeMachine:
	def __init__(self):
		self.count = 0

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.price = 0.90
			self.name = "empty cup"
		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.count = 0
		print("This coffee machine has been repaired.")

	def serve(self, drink : HotBeverage):
		if self.count > 10:
			raise CoffeeMachine.BrokenMachineException()
		self.count += 1
		r = random.randint(0, 1)
		if r == 1:
			return drink
		return CoffeeMachine.EmptyCup()

def main():
	beverages = [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]
	machine = CoffeeMachine()
	for i in range(2):
		print('\n', "Start machine!", '\n')
		try:
			for i in range(12):
				print('iter:', i)
				print(machine.serve(beverages[random.randint(0, 4)]), '\n')
		except Exception as e:
			print(e)
			machine.repair()


if __name__ == "__main__":
	main()


