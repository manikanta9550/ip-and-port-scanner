import socket
import concurrent.futures

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(ip, ports):
    print(f"Scanning ports for {ip}...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    port_range = input("Enter port range (e.g., '1-1000'): ")

    start_port, end_port = map(int, port_range.split('-'))
    ports = range(start_port, end_port + 1)

    scan_ports(target_ip, ports)
~

