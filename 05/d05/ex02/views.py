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
			 	CREATE TABLE if NOT EXISTS ex02_movies(
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

def populate(request):
	movies = [
		{
			"episode_nb": 1,
			"title": "The Phantom Menace",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "1999-05-19"
		},
		{
			"episode_nb": 2,
			"title": "Attack of the Clones",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2002-05-16"
		},
		{
			"episode_nb": 3,
			"title": "Revenge of the Sith",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2005-05-19"
		},
		{
			"episode_nb": 4,
			"title": "A New Hope",
			"director": "George Lucas",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1977-05-25"
		},
		{
			"episode_nb": 5,
			"title": "The Empire Strikes Back",
			"director": "Irvin Kershner",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1980-05-17"
		},
		{
			"episode_nb": 6,
			"title": "Return of the Jedi",
			"director": "Richard Marquand",
			"producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
			"release_date": "1983-05-25"
		},
		{
			"episode_nb": 7,
			"title": "The Force Awakens",
			"director": "J. J. Abrams",
			"producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
			"release_date": "2015-12-11"
		}
	]
	insert = '''
		INSERT INTO ex02_movies
			(
				episode_nb,
				title,
				director,
				producer,
				release_date
			)
			VALUES
			(
				%s, %s, %s, %s, %s
			);
		'''
	result = []
	try:
		connection = psycopg2.connect(
		database='djangotraining',
		user='djangouser',
		password='secret',
		host='127.0.0.1',
		port='5433',
	)
		try:
			connection.autocommit = True
			for movie in movies:
				with connection.cursor() as curs:
					try:
						curs.execute(insert, [
							movie['episode_nb'],
							movie['title'],
							movie['director'],
							movie['producer'],
							movie['release_date'],
						])
						result.append('OK<br>')
					except Exception as e:
						result.append(e.__str__() + '<br>')
		except psycopg2.DatabaseError as e:
			connection.rollback()
			result.append(e.__str__() + '<br>')
		return HttpResponse(result)
	except Exception as e:
		print("[INFO] Error while working with PostgreSQL ", e)
		return HttpResponse(e)

def display(request):
	try:
		connection = psycopg2.connect(
			database='djangotraining',
			user='djangouser',
			password='secret',
			host='127.0.0.1',
			port='5433',
		)
		with connection.cursor() as curs:
			curs.execute('SELECT * FROM ex02_movies;')
			movies = curs.fetchall()
		return render(request, 'ex02/display.html', {"movies": movies})
	except Exception as e:
		return HttpResponse('No data available')
