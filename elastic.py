from elasticsearch import Elasticsearch


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return _es


def store_record(elastic_object, index_name, record):
    elastic_object.index(index=index_name, doc_type='cars', body=record)


def run(summons_number, plate_id, registration_state, plate_type, issue_date,
        violation_code, vehicle_body_type, vehicle_make, issuing_agency):
    es = connect_elasticsearch()
    json = {"summons_number": summons_number,
            "plate_id": plate_id,
            "registration_state": registration_state,
            "plate_type": plate_type,
            "issue_date": issue_date,
            "violation_code": violation_code,
            "vehicle_body_type": vehicle_body_type,
            "vehicle_make": vehicle_make,
            "issuing_agency": issuing_agency}

    store_record(es, 'car_data3', json)
