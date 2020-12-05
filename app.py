from flask import Flask

from dbmanipulation import select_data_from_city, select_all_data_from_city
from statisticdataanalyzer import make_basic_anal, prepare_data_for_chart

app = Flask(__name__)


# endpoint for health checker
@app.route('/ping')
def pingpong():
    return 'pong'


# endpoint returning json raw data for charts
@app.route('/city=<city>&startdate=<startdate>&enddate=<enddate>')
def get_data_for_charts(city, startdate, enddate):
    try:
        return prepare_data_for_chart(select_data_from_city(city, startdate, enddate))
    except Exception as failure:
        print(failure)
        return '{Data Not Available}'


# endpoint returning json data with statistical analysis of selected time period and city (Krakow or Brussels)
@app.route('/statistic&city=<city>&startdate=<startdate>&enddate=<enddate>')
def get_stat_data(city, startdate, enddate):
    try:
        return make_basic_anal(select_data_from_city(city, startdate, enddate))
    except Exception as failure:
        print(failure)
        return '{Data Not Available}'


# endpoint returning json data with statistical analysis from selected city (Krakow or Brussels)
@app.route('/statistic&city=<city>')
def get_stat_data(city):
    try:
        return make_basic_anal(select_all_data_from_city(city))
    except Exception as failure:
        print(failure)
        return '{Data Not Available}'


if __name__ == '__main__':
    app.run()
