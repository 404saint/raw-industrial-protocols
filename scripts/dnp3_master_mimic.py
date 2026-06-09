import socket
import time

# Configuration
TARGET_IP = '127.0.0.1'
PORT = 20000  # Official DNP3 TCP port

# Raw Hex Hex breakdown of a DNP3 Link Status Request:
# Data Link Layer (LPDU):
#   05 64 (Sync Bytes)
#   05    (Length of remaining data link bytes = 5)
#   C9    (Control Byte: Primary frame, Master-to-Outstation, Link Status Request)
#   00 01 (Destination Address = 1)
#   00 02 (Source Address = 2)
#   3B D6 (Data Link Layer CRC-16 Checksum)
DNP3_LINK_STATUS_REQ = b'\x05\x64\x05\xC9\x00\x01\x00\x02\x3B\xD6'

def send_dnp3_frame():
    print(f"Connecting to local listener on {TARGET_IP}:{PORT}...")
    
    # We will use a standard TCP socket stream to inject the payload
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((TARGET_IP, PORT))
            print("TCP Connection established. Injecting raw DNP3 Link Status Request...")
            
            # Send the raw link layer hex bytes
            s.sendall(DNP3_LINK_STATUS_REQ)
            print(f"Sent: {DNP3_LINK_STATUS_REQ.hex().upper()}")
            
            # Keep open briefly to allow tshark to catch the frame teardown
            time.sleep(1)
        except ConnectionRefusedError:
            print(f"Error: Couldn't connect. Make sure tshark or a listener is active on port {PORT}.")

if __name__ == "__main__":
    send_dnp3_frame()