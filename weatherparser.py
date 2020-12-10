import json


def parse_weather_to_json(data_from_db):
    weather_dict={}

    for data in data_from_db:
        weather_dict[data[0]] = {}
        weather_dict[data[0]]['date-time'] = str(data[1])
        weather_dict[data[0]]['temp'] = float(data[2])
        weather_dict[data[0]]['realfeel'] = float(data[3])
        weather_dict[data[0]]['dew_point'] = float(data[4])
        weather_dict[data[0]]['humidity'] = int(data[5])
        weather_dict[data[0]]['wind'] = float(data[6])
        weather_dict[data[0]]['wind_gust'] = float(data[7])
        weather_dict[data[0]]['wind_direction'] = str(data[8])
        weather_dict[data[0]]['rain_chance'] = float(data[9])
        weather_dict[data[0]]['rain_prediction'] = float(data[10])
        weather_dict[data[0]]['snow_chance'] = float(data[11])
        weather_dict[data[0]]['snow_prediction'] = float(data[12])
        weather_dict[data[0]]['ice_chance'] = float(data[13])
        weather_dict[data[0]]['ice_prediction'] = float(data[14])

    return json.dumps(weather_dict)

