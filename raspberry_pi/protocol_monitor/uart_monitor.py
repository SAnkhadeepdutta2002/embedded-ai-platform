import serial
import json
from datetime import datetime

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 115200

LOG_FILE = "../../logs/raw/uart.jsonl"

ser = serial.Serial(
    SERIAL_PORT,
    BAUD_RATE,
    timeout=1
)

print(f"Listening on {SERIAL_PORT}")

while True:

    try:
        raw = ser.readline().decode(
            errors="ignore"
        ).strip()

        if not raw:
            continue

        # Ignore garbage packets
        if not raw.startswith("AA55|"):
            print(f"Ignored: {raw}")
            continue

        fields = raw.split("|")

        if len(fields) != 4:
            print(f"Malformed Packet: {raw}")
            continue

        sync = fields[0]
        packet_id = fields[1]
        payload = fields[2]
        crc = fields[3]

        timestamp = datetime.now().isoformat()

        event = {
            "timestamp": timestamp,
            "sync": sync,
            "packet_id": int(packet_id),
            "payload": payload,
            "crc": crc
        }

        print(event)

        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")

    except Exception as e:
        print(f"Error: {e}")