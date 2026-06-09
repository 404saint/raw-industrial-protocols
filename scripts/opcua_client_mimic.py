import socket
import time

TARGET_IP = '127.0.0.1'
PORT = 4840  # Default OPC UA Binary Port

# Raw OPC UA Binary HEL (Hello) message layout:
# Message Type: "HEL" + Chunk Type: "F" (Final) = b'HELF'
# Message Size: 0x00000020 (32 bytes total length)
# Protocol Version: 0x00000000
# Receive Buffer Size: 0x00010000 (65536)
# Send Buffer Size: 0x00010000 (65536)
# Max Message Size: 0x00000000 (Unassigned/Unlimited)
# Max Chunk Count: 0x00000000 (Unassigned/Unlimited)
# Fully padded 32-byte OPC UA Hello Structure
OPCUA_HEL_REQUEST = (
    b'HELF'                 # 0-3: Message Type + Chunk Type
    b'\x20\x00\x00\x00'     # 4-7: Total Packet Length (32)
    b'\x00\x00\x00\x00'     # 8-11: Protocol Version (0)
    b'\x00\x00\x01\x00'     # 12-15: Receive Buffer Size (65536)
    b'\x00\x00\x01\x00'     # 16-19: Send Buffer Size (65536)
    b'\x00\x00\x01\x00'     # 20-23: Max Message Size (65536)
    b'\x00\x00\x01\x00'     # 24-27: Max Chunk Count (65536)
    b'\x00\x00\x00\x00'     # 28-31: Extra Padding Bounds
)

def send_opcua_packet():
    print(f"Connecting to OPC UA Target on {TARGET_IP}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((TARGET_IP, PORT))
            print("Connected. Injecting OPC UA Binary Hello (HEL) frame...")
            s.sendall(OPCUA_HEL_REQUEST)
            print(f"Sent Hex: {OPCUA_HEL_REQUEST.hex().upper()}")
            time.sleep(1)
        except ConnectionRefusedError:
            print(f"Ensure port {PORT} is listening or being tracked properly.")

if __name__ == "__main__":
    send_opcua_packet()