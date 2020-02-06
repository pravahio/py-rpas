from rpas.fl import FlightLog
from rpas.pa import RPASPermission

def main():

    pa = RPASPermission()

    # Will generate random permission artefact
    permission_artefact = pa.request_permission()

    # You can add a custom id and boundary polygon
    # permission_artefact = pa.request_permission({
    #     'id': '949163bf-e89a-4c8d-8704-76bd48d2bade',
    #     'boundary': [
    #         (12.456487, 77.4875643),
    #         (12.457633, 77.2837287),
    #         (12.378468, 77.2635273)
    #     ]
    # })

    log = FlightLog(permission_artefact)

    # Update current location. FlightLog will log if
    # point is outside the boundary or if time limit expire.
    log.update_current_position(12.5463, 77.7635, 0.5443, FlightLog.State.Takeoff)
    log.update_current_position(12.6453, 77.7354, 5.2736) # Lat, Lon, Alt
    # ...
    log.update_current_position(12.9574, 77.2735, 0.0342, FlightLog.State.Land)
    
    # Get JSON representation of the logs
    json_logs = log.get_json_string()

    print(json_logs)

if '__main__' == __name__:
    main()