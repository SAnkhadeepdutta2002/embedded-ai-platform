import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from fault_engine.fault_manager import FaultManager

manager = FaultManager()

packet = {
    "packet_id": 1,
    "payload": "TEMP:28",
    "crc": "9999"
}

events = manager.analyze(packet)

print(events)