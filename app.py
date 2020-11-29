from flask import Flask

from dbmanipulation import select_data_from_city
from jsonparser import parse_data_in_json

app = Flask(__name__)




@app.route('/')
def example():
   return '{"name":"Bob"}'

@app.route('/ping')
def pingpong():
    return 'pong'

@app.route('/city=<city>&startdate=<startdate>&enddate=<enddate>')
def get_args(city,startdate,enddate):
    json_to_be_send = parse_data_in_json(select_data_from_city(city,startdate,enddate))
    return '{}:'.format(city),json_to_be_send

if __name__ == '__main__':
    app.run()

