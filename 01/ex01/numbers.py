#перед пушем не забудь удалить txt

def read_f():
	f = open("numbers.txt", 'r')
	line = f.read()
	a = line.strip().split(",")
	for i in a:
		print(i)
	f.close()

if __name__ == '__main__':
	read_f()
