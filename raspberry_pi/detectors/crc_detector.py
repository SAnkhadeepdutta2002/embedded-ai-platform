class CRCDetector:

    def analyze(self, packet):

        events = []

        received_crc = packet["crc"]

        expected_crc = "1234"

        if received_crc != expected_crc:

            events.append(
                {
                    "event": "CRC_ERROR",
                    "expected_crc": expected_crc,
                    "received_crc": received_crc
                }
            )

        return events