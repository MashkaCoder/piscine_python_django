import sys
import re

def check_args():
	if len(sys.argv) != 2:
		raise Exception('Wrong number of arguments!')
	if not sys.argv[1].endswith('.template'):
		raise Exception('Wrong extension! You need .template')

def read_tpl():
	file = open(sys.argv[1])
	tpl = file.read()
	file.close()
	return tpl

def read_settings():
	file = open('settings.py', 'r')
	values = {}
	for line in file.readlines():
		lines = line.split('=')
		values[lines[0].strip()] = lines[1].strip().strip('\"')
	file.close()
	return values

def main():
	try:
		check_args()
		tpl = read_tpl()
		val = read_settings()
		file = open("CV.html", 'w')
		file.write(tpl.format(**val))
		file.close()
	except Exception as e:
		print('Error:', e)

if __name__ == "__main__":
	main()
