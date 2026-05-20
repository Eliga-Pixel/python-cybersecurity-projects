import socket

# Common ports and their service names
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
}

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")
            print(f"✅ Port {port} is OPEN ({service})")
    except Exception:
        pass

def main():
    target = input("Enter target IP or hostname (e.g. scanme.nmap.org): ")

    try:
        target_ip = socket.gethostbyname(target)
        print(f"\nScanning {target} ({target_ip})...")
        print("-" * 40)

        for port in range(1, 1025):
            scan_port(target_ip, port)

        print("\nScan complete.")
    except socket.gaierror:
        print("❌ Could not resolve the hostname.")

if __name__ == "__main__":
    main()