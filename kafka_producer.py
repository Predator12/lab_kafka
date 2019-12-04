import json
from kafka import KafkaProducer
from time import sleep

from settings import settings


class Kafka:

    @staticmethod
    def send_data(summons_number, plate_id, registration_state, plate_type, issue_date,
                  violation_code, vehicle_body_type, vehicle_make, issuing_agency, row_id):
        producer = KafkaProducer(
            bootstrap_servers=["{}:{}".format(settings.CONFIG['KAFKA_HOST'], settings.CONFIG['KAFKA_PORT'])],
            value_serializer=lambda x: json.dumps(x).encode("utf-8"))

        data = {'id': row_id,
                'summons_number': summons_number,
                'plate_id': plate_id,
                'registration_state': registration_state,
                'plate_type': plate_type,
                'issue_date': issue_date,
                'violation_code': violation_code,
                'vehicle_body_type': vehicle_body_type,
                'vehicle_make': vehicle_make,
                'issuing_agency': issuing_agency}

        if settings.CONFIG['KAFKA_TOPIC_ID'] == 1:
            topic_name = '24topik'
        elif settings.CONFIG['KAFKA_TOPIC_ID'] == 2:
            topic_name = '5topic'
        else:
            topic_name = '5min'
        producer.send(topic_name, data)
        print("row{}".format(row_id))
