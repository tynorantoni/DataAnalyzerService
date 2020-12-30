import json



def parse_health_result_to_json(data_from_db):
    result_value={}
    for data in data_from_db:
        result_value['date-time']=data[1].strftime("%d-%m-%Y, %H:%M:%S")
        result_value['BSS']=data[2]
        result_value['KSS']=data[3]
        result_value['WCS']=data[4]
        result_value['DAS']=data[5]
        result_value['UIS']=data[6]

    return json.dumps(result_value)


