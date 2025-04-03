import random
import time
import serial

def simulate_heartbeat():
    ser = serial.Serial('COM3', 115200)  # VS'deki sanal port
    while True:
        hr = random.randint(20, 200)
        print(f"SIM: Heartbeat {hr} BPM")
        if hr < 30:
            ser.write(b'T')  # Acil durum sinyali
        time.sleep(2)

if __name__ == "__main__":
    simulate_heartbeat()