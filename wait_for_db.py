import socket
import time
import sys

def check_db():
    """
    Check if the database is ready to accept connections.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(("db", 3306))
        sock.close()
        return result == 0
    except:
        return False

print("Waiting for database to be ready...")
while not check_db():
    print(".", end="", flush=True)
    time.sleep(1)
print("\nDatabase is ready!")
time.sleep(5) 