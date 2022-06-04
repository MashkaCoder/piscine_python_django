from path import Path

def main():
	try:
		Path.makedirs('ssssschool')
		Path.touch('ssssschool/chasimir')
		f = Path('ssssschool/chasimir')
		f.write_lines(['Chasimir', 'top'])
		print(f.read_text())
	except FileExistsError as e:
		print(e)


if __name__ == '__main__':
	main()
