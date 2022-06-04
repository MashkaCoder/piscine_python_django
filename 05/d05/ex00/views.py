from django.db import connection
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import psycopg2

# Create your views here.
def init(request):
	try:
		connection = psycopg2.connect(
			host = '127.0.0.1',
			user = 'djangouser',
			password = 'secret',
			database = 'djangotraining',
			port = '5433'
		)
		connection.autocommit = True
		with connection.cursor() as cursor:
			cursor.execute("""
			 	CREATE TABLE if NOT EXISTS ex00_movies(
				title VARCHAR(64) UNIQUE NOT NULL,
				episode_nb INT PRIMARY KEY,
				opening_crawl TEXT,
				director VARCHAR(32) NOT NULL,
				producer VARCHAR(128) NOT NULL,
				release_date DATE NOT NULL
				);
			"""
			)
		return HttpResponse("OK")
	except Exception as e:
		print("[INFO] Error while working with PostgreSQL ", e)
		return HttpResponse(e)

