import kafka_producer
import logs
from settings import settings


class ExportDestinationSelector:
    def __init__(self):
        self.EXPORT_TYPE_MAPPER = {
            'kafka': kafka_producer.Kafka,
            'logs': logs.Log
        }

    def send_data(self, summons_number, plate_id, registration_state, plate_type, issue_date,
                  violation_code, vehicle_body_type, vehicle_make, issuing_agency, row_id):
        export_source_name = settings.CONFIG('EXPORT_DESTINATION')

        self.EXPORT_TYPE_MAPPER[export_source_name].send_data(summons_number, plate_id, registration_state, plate_type,
                                                              issue_date, violation_code, vehicle_body_type,
                                                              vehicle_make, issuing_agency, row_id)
