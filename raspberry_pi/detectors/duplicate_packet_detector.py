class DuplicatePacketDetector:

    def __init__(self):
        self.last_packet_id = None

    def analyze(self, packet):

        events = []

        packet_id = packet["packet_id"]

        if packet_id == self.last_packet_id:

            events.append({
                "event": "DUPLICATE_PACKET",
                "packet_id": packet_id
            })

        self.last_packet_id = packet_id

        return events