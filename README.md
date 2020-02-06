### Module to generate DigitalSky compatible flight logs and permission artefacts.
**This module is still work in progress and the APIs might change in the future.**

This module follows protobuf definition available here: [Flight Logs and Permission Artefact](https://github.com/pravahio/protocols/tree/rpas/protocols/rpas-india)

#### Installation
```
pip install rpas
```

#### Usage
```py
from rpas.fl import FlightLog
from rpas.pa import RPASPermission

def main():

    pa = RPASPermission()

    # Generate random permission artefact
    permission_artefact = pa.request_permission()

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
```

#### JSON Output for flight logs
```json
{
  "flightLog": {
    "permissionArtefact": "949163bf-e89a-4c8d-8704-76bd48d2bade",
    "logEntries": [
      {
        "entryType": "TAKEOFF_ARM",
        "timestamp": "1580989885",
        "longitude": 77.7635,
        "latitude": 12.5463,
        "altitude": 0.5443
      },
      {
        "entryType": "TIME_BREACH",
        "timestamp": "1580989885",
        "longitude": 77.7354,
        "latitude": 12.6453,
        "altitude": 5.2736
      },
      {
        "entryType": "LAND_DISARM",
        "timestamp": "1580989885",
        "longitude": 77.2735,
        "latitude": 12.9574,
        "altitude": 0.0342
      }
    ]
  }
}
```