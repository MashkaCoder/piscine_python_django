import sys
import requests
from bs4 import BeautifulSoup

class PhilosophyFinder:
	def __init__(self):
		self.titles = []

	def search_philo(self, title_str):
		url = f'https://en.wikipedia.org/{title_str}'
		try:
			res = requests.get(url)
			res.raise_for_status()
		except requests.HTTPError as e:
			if res.status_code == 404:
				print("It\'s a dead end !")
				return
			print(e)
			return
		parser = BeautifulSoup(res.text, 'html.parser')
		title = parser.find(id='firstHeading').text
		if title in self.titles:
			print("It will become an infinite loop!")
			return
		self.titles.append(title)
		print(title)
		if title == 'Philosophy' and len(self.titles) > 1:
			print(f'{len(self.titles) - 1} roads from {sys.argv[1]} to philosophy')
			return
		content = parser.find(id='mw-content-text')
		all_links = content.select('p > a')
		for link in all_links:
			if link.get('href') is not None and link['href'].startswith('/wiki/') \
					and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
				self.search_philo(link['href'])
				return
		print("It\'s a dead end !")

def check_args():
	if len(sys.argv) != 2:
		raise Exception("Wrong arguments")

def main():
	try:
		check_args()
		PhilosophyFinder().search_philo('/wiki/' + sys.argv[1])
	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	main()
