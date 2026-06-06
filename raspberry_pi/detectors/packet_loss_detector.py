import json


class PacketLossDetector:

    def __init__(self):
        self.last_packet_id = None

    def analyze(self, packet):

        events = []

        packet_id = packet["packet_id"]

        if self.last_packet_id is not None:

            expected_packet = self.last_packet_id + 1

            if packet_id > expected_packet:

                events.append({
                    "event": "PACKET_LOSS",
                    "expected_packet": expected_packet,
                    "received_packet": packet_id
                })

        self.last_packet_id = packet_id

        return events