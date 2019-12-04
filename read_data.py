import datetime
import redis
import requests
import elastic

from strategy import ExportDestinationSelector
from settings import settings


class Data:
    COMPLETED_STATUS = 'COMPLETED'

    def __init__(self, url):
        self.url = url

    def read(self):
        rows_count = 0
        data_limit = 1000
        # redis_db = redis.Redis(host=settings.CONFIG['REDIS_HOST'], port=settings.CONFIG['REDIS_PORT'], db=0)
        current_time = str(datetime.datetime.now())

        # if redis_db.lindex(self.url, 0):
        #     data_status = redis_db.lindex(self.url, 0).decode('utf-8')
        # else:
        #     data_status = ''

        if "" == self.COMPLETED_STATUS:
            print('Data already exists')
        else:
            data = requests.get(self.url).json()
            # redis_db.lpush(self.url, current_time)

            for row in range(data_limit):
                rows_count += 1
                summons_number = data[row].get('summons_number')
                plate_id = data[row].get('plate_id')
                registration_state = data[row].get('registration_state')
                plate_type = data[row].get('plate_type')
                issue_date = data[row].get('issue_date')
                violation_code = data[row].get('violation_code')
                vehicle_body_type = data[row].get('vehicle_body_type')
                vehicle_make = data[row].get('vehicle_make')
                issuing_agency = data[row].get('issuing_agency')
                print("rows{}".format(rows_count))
                export_source = ExportDestinationSelector()
                export_source.send_data(summons_number, plate_id, registration_state, plate_type, issue_date,
                                        violation_code, vehicle_body_type, vehicle_make, issuing_agency, rows_count)
                print("rows{}".format(rows_count))
                # elastic.run(summons_number, plate_id, registration_state, plate_type, issue_date,
                #             violation_code, vehicle_body_type, vehicle_make, issuing_agency)

            #     if rows_count % 100 == 0:
            #         redis_db.lpush(self.url, "{}-{}".format(rows_count - 99, rows_count))
            # redis_db.lpush(self.url, self.COMPLETED_STATUS)
