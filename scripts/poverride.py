import time
from pymodbus.client import ModbusTcpClient

PLC_IP = "192.168.204.133"
PLC_PORT = 502
COIL_ADDRESS = 0

client = ModbusTcpClient(PLC_IP, port=PLC_PORT)

if client.connect():
    print(f"Connected to OpenPLC at {PLC_IP}:{PLC_PORT}")

    end_time = time.time() + 5

    while time.time() < end_time:
        client.write_coil(COIL_ADDRESS, False)
        time.sleep(0.05)

    client.close()
else:
    print("Connection failed")