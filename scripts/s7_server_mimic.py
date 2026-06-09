import socket

HOST = '127.0.0.1'
PORT = 102  # Official Siemens S7 Port

# Raw COTP Connection Confirm response
# TPKT: 03 00 00 16 (Version 3, length 22)
# COTP: 11 d0 (Length 17, Connection Confirm) ...
S7_COTP_CONFIRM = b'\x03\x00\x00\x16\x11\xd0\x00\x01\x00\x02\x00\xc0\x01\x0a\xc1\x02\x01\x00\xc2\x02\x02\x00'

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Mock Siemens PLC listening on {HOST}:{PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"S7 connection request from {addr}")
            data = conn.recv(1024)
            if data:
                print(f"Received Request Hex: {data.hex().upper()}")
                conn.sendall(S7_COTP_CONFIRM)
                print("Sent S7 COTP Connection Confirmation.")

if __name__ == "__main__":
    run_server()