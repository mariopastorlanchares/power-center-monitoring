import os
import requests
import configparser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


script_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar configuración
config = configparser.ConfigParser()
config.read('config.ini')

# Configuración de Firebase
cred_path = os.path.join(script_dir, 'credentials.json')
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': config['DEFAULT']['FirebaseRealtimeDatabaseUrl']
})

serial_nos = config['DEFAULT']['SerialNos'].split(',')
firebase_user_id = config['DEFAULT']['FirebaseUserId']
last_timestamp_file = os.path.join(script_dir, 'last_timestamp.txt')

# Leer el último timestamp guardado
try:
    with open(last_timestamp_file, 'r') as file:
        last_timestamp = file.read().strip()
except FileNotFoundError:
    last_timestamp = None

new_timestamp = None

# URL del endpoint
url = "http://power-datacenter.com/cmc/getWorkInfo.html?random=0.7550451473317242"

for i, serial_no in enumerate(serial_nos, start=1):
    serial_no = serial_no.strip()

    # Datos para la petición POST
    payload = {
        'serialNo': serial_no,
        'protocol': 30
    }

    # Realizar petición POST
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        data = response.json()
        timestamp = data.get('time', {}).get('time')
        # Eliminar datos no deseados
        keys_to_remove = [
            'time',
            'chargeSource',
            'prodid',
            'workMode',
            'loadSource',
            'dataID',
            'serialNo',
            'serverTimestr'
        ]
        for key in keys_to_remove:
            data.pop(key, None)

        if timestamp and str(timestamp) != str(last_timestamp):
            new_timestamp = timestamp
            # Guardar datos en Firebase
            ref = db.reference(f'/{firebase_user_id}/{timestamp}/inverter_{i}')
            ref.set(data)
        else:
            print(f"Datos ya actualizados para el inversor {serial_no}")

# Guardar el nuevo timestamp
if new_timestamp:
    with open(last_timestamp_file, 'w') as file:
        file.write(str(new_timestamp))
