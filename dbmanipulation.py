import psycopg2
from dbconnector import connect_to_db


# return dataset from DB from Krakow or Brussels
def select_data_from_city(city, start_date, end_date):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if city == 'krk':
            cur.execute(
                '''SELECT * FROM krakow_data WHERE (date_of_count >= '{}' AND date_of_count <= '{}');'''.format(
                    start_date, end_date
                ))
            conn.commit()
            desired_data = cur.fetchall()
        elif city == "br":
            cur.execute(
                '''SELECT * FROM brussels_data WHERE (date_of_count >= '{}' AND date_of_count <= '{}');'''.format(
                    start_date, end_date
                ))

            conn.commit()
            desired_data = cur.fetchall()
        return desired_data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error

    finally:
        cur.close()
        conn.close()


# return all data from selected city (Krakow or Brussels)
def select_all_data_from_city(city):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if city == 'krk':
            cur.execute(
                '''SELECT * FROM krakow_data;''')
            conn.commit()
            desired_data = cur.fetchall()
        elif city == "br":
            cur.execute(
                '''SELECT * FROM brussels_data;''')

            conn.commit()
            desired_data = cur.fetchall()
        return desired_data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error

    finally:
        cur.close()
        conn.close()

def select_last_3_hours_from_weather():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute(
            '''SELECT * FROM weather_data ORDER BY id DESC LIMIT 3;''')
        conn.commit()
        desired_data = cur.fetchall()

        return desired_data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error

    finally:
        cur.close()
        conn.close()

