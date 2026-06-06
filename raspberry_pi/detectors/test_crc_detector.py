from crc_detector import CRCDetector

detector = CRCDetector()

packet = {
    "packet_id": 1,
    "crc": "9999"
}

events = detector.analyze(packet)

print(events)