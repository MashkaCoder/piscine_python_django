
class Intern:
	def __init__(self, name=None):
		self.name = name
		if name == None:
			self.name = "My name? I'm nobody, an intern, I have no name."
	def __str__(self):
		return self.name
	def work(self):
		raise Exception("I'm just an intern, I can't do that...")
	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."
	def make_coffee(self):
		return Intern.Coffee()


def main():
	noname = Intern()
	Rail = Intern("Rail")
	print(noname.__str__())
	print(Rail.__str__())
	print(Rail.make_coffee())
	try:
		Rail.work()
	except Exception as e:
		print('Error:', e)


if __name__ == '__main__':
	main()
