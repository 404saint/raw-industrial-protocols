import socket

HOST = '127.0.0.1'
PORT = 44818

# Mock EtherNet/IP Registration Response
# Command: 0065 (Register Session), Length: 0004, Session Handle: 12345678, Status: 00000000...
EIP_REGISTER_RESPONSE = (
    b'\x00\x65\x00\x04\x12\x34\x56\x78\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x01\x00\x00'
)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Mock EtherNet/IP Target listening on {HOST}:{PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Engineering workstation connected from {addr}")
            data = conn.recv(1024)
            if data:
                print(f"Received Request Hex: {data.hex().upper()}")
                conn.sendall(EIP_REGISTER_RESPONSE)
                print("Dispatched valid Session Handle (0x12345678).")

if __name__ == "__main__":
    run_server()