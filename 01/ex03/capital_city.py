import sys

def search_cap_city():
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
		key = states.get(sys.argv[1])
		if not key:
			print("Unknown state")
			return
		print(capital_cities.get(key))

if __name__ == "__main__":
	search_cap_city()
