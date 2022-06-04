def my_sort():
	d={
	'Hendrix' : '1942', 'Allman' : '1946',
	'King' : '1925', 'Clapton' : '1945',
	'Johnson' : '1911', 'Berry' : '1926',
	'Vaughan' : '1954', 'Cooder' : '1947',
	'Page' : '1944', 'Richards' : '1943',
	'Hammett' : '1962', 'Cobain' : '1967',
	'Garcia' : '1942', 'Beck' : '1944', 'Santana' : '1947',
	'Ramone' : '1948', 'White' : '1975',
	'Frusciante': '1970', 'Thompson' : '1949',
	'Burton' : '1939',
	}
	sort_d={}

	d = sorted(d)
	min_a = int(d[0])

	for i in range(len(d)):
		for j in range(len(d)):
			if int(d[i]) > d[j]:
				a = d[j]
				d[j] = d[i]
				d[i] = a


	for i in d:
		print(i, ":", d[i])

if __name__ == "__main__":
	my_sort()


print(1)
