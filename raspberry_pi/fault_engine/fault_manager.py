import json
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from detectors.packet_loss_detector import PacketLossDetector
from detectors.duplicate_packet_detector import DuplicatePacketDetector
from event_engine.event_logger import EventLogger
from detectors.crc_detector import CRCDetector


class FaultManager:

    def __init__(self):

        self.detectors = [

            PacketLossDetector(),
            DuplicatePacketDetector(),
            CRCDetector()

        ]

        self.logger = EventLogger()

    def analyze(self, packet):

        all_events = []

        for detector in self.detectors:

            events = detector.analyze(packet)

            if events:
                all_events.extend(events)

        return all_events


if __name__ == "__main__":

    manager = FaultManager()

    packets = [
        {"packet_id": 1},
        {"packet_id": 2},
        {"packet_id": 2},
        {"packet_id": 4}
    ]

    for packet in packets:

        events = manager.analyze(packet)

        if events:

            for event in events:

                print(event)

                manager.logger.log(event)