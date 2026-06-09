import socket

# Configuration
HOST = '127.0.0.1'
PORT = 5020

# Hardcoded Modbus TCP Response Packet for 3 Holding Registers containing [100, 200, 300]
# Hex breakdown:
# MBAP Header:
#   00 01 (Transaction ID)
#   00 00 (Protocol ID = Modbus)
#   00 09 (Length = 9 bytes follow)
#   01    (Unit ID = 1)
# PDU:
#   03    (Function Code = Read Holding Registers)
#   06    (Byte Count = 6 bytes of data follow)
#   00 64 (Register 1 value = 100)
#   00 C8 (Register 2 value = 200)
#   01 2C (Register 3 value = 300)
MODBUS_RESPONSE = b'\x00\x01\x00\x00\x00\x09\x01\x03\x06\x00\x64\x00\xc8\x01\x2c'

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Pure Python Modbus Server listening on {HOST}:{PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Client connected from {addr}")
            data = conn.recv(1024)
            if data:
                print(f"Received raw request: {data.hex()}")
                # Send back our crafted Modbus response
                conn.sendall(MODBUS_RESPONSE)
                print("Sent raw Modbus response.")

if __name__ == "__main__":
    run_server()