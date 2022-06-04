import sys
import antigravity

def check_args():
	if len(sys.argv) != 4:
		raise Exception("Wrong argument")

def main():
	try:
		check_args()
		latitude = float(sys.argv[1])
		longitude = float(sys.argv[2])
		date = sys.argv[3].encode('utf-8')
		antigravity.geohash(latitude, longitude, date)
	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	main()
