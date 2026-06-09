import socket
import time

TARGET_IP = '127.0.0.1'
PORT = 102

# Raw TPKT + COTP Connection Request (CR) packet
S7_COTP_REQUEST = b'\x03\x00\x00\x16\x11\xe0\x00\x00\x00\x01\x00\xc0\x01\x0a\xc1\x02\x01\x00\xc2\x02\x02\x00'

def send_s7_packet():
    print(f"Connecting to Siemens target on {TARGET_IP}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((TARGET_IP, PORT))
            print("Connected. Sending COTP Connection Request...")
            s.sendall(S7_COTP_REQUEST)
            print(f"Sent Hex: {S7_COTP_REQUEST.hex().upper()}")
            time.sleep(1)
        except ConnectionRefusedError:
            print("Connection failed. Check your port 102 configuration.")

if __name__ == "__main__":
    send_s7_packet()