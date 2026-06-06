import json
from datetime import datetime


class EventLogger:

    def __init__(self):

        self.log_file = "../../logs/faults/events.jsonl"

    def log(self, event):

        event["timestamp"] = datetime.now().isoformat()

        with open(self.log_file, "a") as f:

            f.write(json.dumps(event) + "\n")