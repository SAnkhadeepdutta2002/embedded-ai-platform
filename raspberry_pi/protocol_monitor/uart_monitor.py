import serial
import json
import time
from datetime import datetime
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from fault_engine.fault_manager import FaultManager

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 115200

LOG_FILE = "/home/pi/Projects/embedded-ai-platform/logs/raw/uart.jsonl"

manager = FaultManager()


def connect_serial():

    while True:

        try:

            print(f"Waiting for ESP32 on {SERIAL_PORT}...")

            ser = serial.Serial(
                SERIAL_PORT,
                BAUD_RATE,
                timeout=1
            )

            time.sleep(2)

            print("ESP32 Connected")

            return ser

        except Exception:

            time.sleep(1)


ser = connect_serial()

while True:

    try:

        raw = ser.readline().decode(
            errors="ignore"
        ).strip()

        if not raw:
            continue

        if not raw.startswith("AA55|"):
            continue

        fields = raw.split("|")

        if len(fields) != 4:

            print(f"Malformed Packet: {raw}")
            continue

        packet = {
            "timestamp": datetime.now().isoformat(),
            "sync": fields[0],
            "packet_id": int(fields[1]),
            "payload": fields[2],
            "crc": fields[3]
        }

        print(packet)

        fault_events = manager.analyze(packet)

        if fault_events:

            print("FAULT EVENTS:")

            for event in fault_events:

                event["source"] = "UART"

                print(event)

                manager.logger.log(event)

        with open(LOG_FILE, "a") as f:

            f.write(json.dumps(packet) + "\n")

    except serial.SerialException:

        print("ESP32 Disconnected")

        try:
            ser.close()
        except:
            pass

        ser = connect_serial()

    except Exception as e:

        print("Error:", e)