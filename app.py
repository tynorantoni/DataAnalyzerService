from flask import Flask

from dbmanipulation import select_data_from_city, select_all_data_from_city
from jsonparser import parse_data_in_json
from statisticdataanalyzer import make_basic_anal

app = Flask(__name__)


@app.route('/ping')
def pingpong():
    return 'pong'

@app.route('/city=<city>&startdate=<startdate>&enddate=<enddate>')
def get_data_for_charts(city,startdate,enddate):
    return '{}:{}'.format(city,parse_data_in_json(select_data_from_city(city,startdate,enddate)))\

@app.route('/statistic&city=<city>&startdate=<startdate>&enddate=<enddate>')
def get_stat_data(city,startdate,enddate):
    return make_basic_anal(city, select_data_from_city(city,startdate,enddate))\

@app.route('/statistic&city=<city>')
def get_stat_data(city):
    return make_basic_anal(city, select_all_data_from_city(city))

if __name__ == '__main__':
    app.run()

