from flask import Flask

from dbmanipulation import select_data_from_city, select_all_data_from_city, select_last_3_hours_from_weather, \
    select_last_health_status
from healthparser import parse_health_result_to_json
from statisticdataanalyzer import make_basic_anal, prepare_data_for_chart
from weatherparser import parse_weather_to_json

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
def get_all_stat_data(city):
    try:
        return make_basic_anal(select_all_data_from_city(city))
    except Exception as failure:
        print(failure)
        return '{Data Not Available}'

# endpoint returning json weather data
@app.route('/forecast')
def get_weather_data():
    try:
        return parse_weather_to_json(select_last_3_hours_from_weather())[0]
    except Exception as failure:
        print(failure)
        return '{Data Not Available}'

# endpoint returning json weather alerts data
@app.route('/alerts')
def get_weather_alerts():
    try:
        return parse_weather_to_json(select_last_3_hours_from_weather())[1]
    except Exception as failure:
        print(failure)
        return '{Data Not Available}'

@app.route('/health-stats')
def get_health_stats():
    try:
        return parse_health_result_to_json(select_last_health_status())
    except:
        return '{Data Not Available}'

if __name__ == '__main__':
    app.run()
