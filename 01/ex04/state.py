import sys

def search_st():
	if len(sys.argv) == 2:
		states = {
			"Oregon" : "OR",
			"Alabama" : "AL",
			"New Jersey": "NJ",
			"Colorado" : "CO"
		}

		capital_cities = {
			"OR": "Salem",
			"AL": "Montgomery",
			"NJ": "Trenton",
			"CO": "Denver"
		}
		value = 1
		for i in states:
			if i == sys.argv[1]:
				value = states[i]
		if value == 1:
			print("Unknown capital city")
			return
		for i in capital_cities:
			if i == value:
				print(capital_cities[i])


if __name__ == "__main__":
	search_st()
