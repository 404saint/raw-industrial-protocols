import socket

HOST = '127.0.0.1'
PORT = 4840

# Raw OPC UA Binary ACK (Acknowledge) message layout:
# Message Type: "ACK" + Chunk Type: "F" (Final) = b'ACKF'
# Message Size: 0x00000020 (32 bytes total length)
# Protocol Version: 0x00000000
# Receive Buffer Size: 0x00010000 (65536)
# Send Buffer Size: 0x00010000 (65536)
# Max Message Size: 0x00000000 (Unlimited)
# Max Chunk Count: 0x00000000 (Unlimited)
OPCUA_ACK_RESPONSE = (
    b'ACKF'
    b'\x20\x00\x00\x00'
    b'\x00\x00\x00\x00'
    b'\x00\x00\x01\x00'
    b'\x00\x00\x01\x00'
    b'\x00\x00\x00\x00'
    b'\x00\x00\x00\x00'
)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Mock OPC UA Endpoint listening on {HOST}:{PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"OPC UA connection established from {addr}")
            data = conn.recv(1024)
            if data:
                print(f"Received Handshake Hex: {data.hex().upper()}")
                conn.sendall(OPCUA_ACK_RESPONSE)
                print("Dispatched OPC UA Binary ACK frame.")

if __name__ == "__main__":
    run_server()