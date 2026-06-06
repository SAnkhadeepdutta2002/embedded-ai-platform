from duplicate_packet_detector import DuplicatePacketDetector

detector = DuplicatePacketDetector()

packets = [
    {"packet_id": 1},
    {"packet_id": 2},
    {"packet_id": 2},
    {"packet_id": 3}
]

for packet in packets:

    events = detector.analyze(packet)

    if events:
        print(events)