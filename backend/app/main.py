import json
from flask import Flask, request
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

server =   '172.17.0.1'
# database = 'GREENITY'
database = 'greenity'
username = 'greenity'
password = 'RiseGreen8y'
port =     '5432'
# driver =   'ODBC Driver 13 for SQL Server'

engine = create_engine('postgresql+psycopg2://' + username + ':' + password + '@' + server + ':' + port + '/' + database, echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route("/")
def hello():
	lat = request.args.get('latitude', type=str)
	lng = request.args.get('longitude', type=str)
	lat_lng_bounds = get_lat_lang_bounds(lat, lng)
	query = '''
		SELECT latitude, longitude, score FROM RSEI
		JOIN grid ON (RSEI.x = grid.x AND RSEI.y = grid.y)
		WHERE latitude < {lat_upper} AND latitude > {lat_lower}
		AND longitude < {lng_upper} AND longitude > {lng_lower}
	'''
	print('About to execute query')
	result = session.execute(query.format(**lat_lng_bounds))
	# print([row for row in result])
	print('Result populated. Now converting.')
	print([dict(row) for row in result])
	return 'request successful'
	# return "Request successful"

@app.route("/echo")
def echo():
    return 'Make me a sandwich'

def get_lat_lang_bounds(latitude, longitude):
	latitude_upper_bound = str(float(latitude) + 0.05)
	latitude_lower_bound = str(float(latitude) - 0.05)
	longitude_upper_bound = str(float(longitude) + 0.05)
	longitude_lower_bound = str(float(longitude) - 0.05)
	return {
		'lat_upper': latitude_upper_bound,
		'lat_lower': latitude_lower_bound,
		'lng_upper': longitude_upper_bound,
		'lng_lower': longitude_lower_bound
	}

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)