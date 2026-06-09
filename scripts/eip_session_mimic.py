import socket
import time

TARGET_IP = '127.0.0.1'
PORT = 44818  # Official EtherNet/IP Port

# Raw Hex breakdown of an EtherNet/IP Session Registration Request:
# Encapsulation Header:
#   00 65 (Command: Register Session)
#   00 04 (Length of command specific data = 4 bytes)
#   00 00 00 00 (Session Handle: 0 for now, the PLC will assign one)
#   00 00 00 00 (Status: Success = 0)
#   00 00 00 00 00 00 00 00 (Sender Context string padding)
#   00 00 00 00 (Options flags)
# Command Specific Data (CIP Protocol Version):
#   00 01 (Protocol Version = 1)
#   00 00 (Option flags = 0)
EIP_REGISTER_SESSION = (
    b'\x00\x65\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x01\x00\x00'
)

def send_eip_packet():
    print(f"Connecting to EtherNet/IP target on {TARGET_IP}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((TARGET_IP, PORT))
            print("Connected. Sending Explicit CIP Encapsulation Register Session Request...")
            s.sendall(EIP_REGISTER_SESSION)
            print(f"Sent Hex: {EIP_REGISTER_SESSION.hex().upper()}")
            time.sleep(1)
        except ConnectionRefusedError:
            print(f"Make sure your tshark or local port listener is tracking port {PORT}.")

if __name__ == "__main__":
    send_eip_packet()