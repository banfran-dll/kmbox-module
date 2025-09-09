import serial
import time

class MkitMouse:
    def __init__(self, port: str, baudrate: int = 115200):
        self.port_name = port
        self.baudrate = baudrate
        self.serial_port = None

    def connect(self):
        try:
            self.serial_port = serial.Serial(self.port_name, self.baudrate, timeout=1)
            time.sleep(2)
        except Exception as e:
            self.serial_port = None
            raise RuntimeError(f"Failed to connect to M-kit: {e}")

    def disconnect(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.serial_port = None

    def is_connected(self) -> bool:
        return self.serial_port is not None and self.serial_port.is_open

    def move(self, dx: int, dy: int):
        if not self.is_connected():
            raise RuntimeError("not connected to M-kit")
        cmd = f"km.move({dx}, {dy})\n"
        self.serial_port.write(cmd.encode('utf-8'))

        time.sleep(0.0001)
