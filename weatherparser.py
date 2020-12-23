import json


def parse_weather_to_json(data_from_db):
    weather_dict={}
    alerts={}
    for data in data_from_db:
        weather_dict[data[0]] = {}
        weather_dict[data[0]]['date-time'] = str(data[1])
        weather_dict[data[0]]['temp'] = float(data[2])
        weather_dict[data[0]]['realfeel'] = float(data[3])
        weather_dict[data[0]]['humidity'] = int(data[5])
        weather_dict[data[0]]['wind'] = float(data[6])
        weather_dict[data[0]]['wind_gust'] = float(data[7])
        weather_dict[data[0]]['wind_direction'] = str(data[8])
        alerts[str(data[1])]={}
        if float(data[9])>0:
            alerts[str(data[1])]['rain']=f'Warning! Rain Prediction {float(data[10])}'
        if float(data[11])>0:
            alerts[str(data[1])]['snow']=f'Warning! Snow Prediction {float(data[12])}'
        if float(data[13])>0:
            alerts[str(data[1])]['ice']=f'Warning! Ice Prediction {float(data[13])}'
        if float(data[4])<0:
            alerts[str(data[1])]['road']="Warning! Black Ice!"

    return json.dumps(weather_dict), json.dumps(alerts)

