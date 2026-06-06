from packet_loss_detector import PacketLossDetector

detector = PacketLossDetector()

packets = [
    {"packet_id": 1},
    {"packet_id": 2},
    {"packet_id": 3},
    {"packet_id": 5}
]

for packet in packets:

    events = detector.analyze(packet)

    if events:
        print(events)