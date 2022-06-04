import requests
import json
import dewiki
import sys

def request_wiki(page:str):
	url = "https://en.wikipedia.org/w/api.php"
	params = {
		"action": "parse",
		"page": page,
		"prop": "wikitext",
		"format": "json",
		"redirects": "true",
		"formatversion": 2
	}
	try:
		res = requests.get(url, params)
		res.raise_for_status()
	except requests.HTTPError as e:
		raise e
	try:
		data_page = json.loads(res.text)
		if data_page.get('error'):
			raise Exception(data_page['error']['info'])
	except Exception as e:
		raise e
	return dewiki.from_string(data_page['parse']['wikitext'])


def check_args():
	if len(sys.argv) != 2:
		raise Exception("Wrong arguments")

def main():
	try:
		check_args()
		data_page = request_wiki(sys.argv[1])
		file = open(sys.argv[1] + '.wiki', 'w')
		file.write(data_page)
		file.close()
	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	main()

