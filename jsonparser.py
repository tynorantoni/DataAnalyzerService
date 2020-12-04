import json



#co tu autor miał na myśli to nie wiem sam
def parse_data_in_json(data_from_db):
    data_dict = {}
    for row in data_from_db:
        data_dict['street_name'] = row[1]
        data_dict['street_name']['date_of_count'] = row[0]
        data_dict['street_name']['day_cnt'] = row[2]

    data_json = json.loads(data_dict)
    return data_json
