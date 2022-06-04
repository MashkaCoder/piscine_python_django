from multiprocessing import Value
from pickle import FALSE
import sys

def search_state(dictionary, state):
	for key in dictionary:
		if key.lower() == state.lower():
			return dictionary[key]
	return None

def search_city(dictionary, city):
	for key, value in dictionary.items():
		if value.lower() == city.lower():
			return key
	return None

def generate_list_dic(argv):
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
	argv_list = argv.lower().split(",")
	for i in range(len(argv_list)):
		argv_list[i] = argv_list[i].strip()
		if not argv_list[i]:
			continue
		state = search_state(states, argv_list[i])
		city = search_city(capital_cities, argv_list[i])
		if state:
			print(capital_cities[state], " is the capital of", search_city(states, state))
		elif city:
			print(capital_cities[city], " is the capital of", search_city(states, city))
		else:
			print(argv_list[i], "is neither a capital city nor a state")

def main():
	if len(sys.argv) == 2:
		generate_list_dic(sys.argv[1])

if __name__ == "__main__":
	main()
