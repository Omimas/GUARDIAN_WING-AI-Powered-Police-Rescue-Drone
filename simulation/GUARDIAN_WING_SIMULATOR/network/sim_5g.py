import socket
import json


class NetworkSimulator:
    def __init__(self):
        self.server = socket.socket()
        self.server.bind(("localhost", 5000))

    def send_emergency_data(self):
        while True:
            data = {
                "type": "emergency",
                "gps": {"lat": 41.0082, "lng": 28.9784}
            }
            self.server.send(json.dumps(data).encode())


if __name__ == "__main__":
    sim = NetworkSimulator()
    sim.send_emergency_data()