import psycopg2

from dbconnector import connect_to_db


def select_data_from_city(city,start_date,end_date):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if city == 'krk':
            desired_data = cur.execute(
                '''SELECT * FROM krakow_data WHERE (date_of_count >= {} AND date_of_count <= {});'''.format(
                start_date,end_date
            ))

            conn.commit()
        elif city == "br":
            desired_data = cur.execute(
                '''SELECT * FROM brussels_data WHERE (date_of_count >= {} AND date_of_count <= {});'''.format(
                    start_date, end_date
                ))

        conn.commit()
        return desired_data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 9999

    finally:
        cur.close()
        conn.close()


