#!/usr/bin/env python3
 
import argparse
import socket
 
 
BROADCAST_IP = "255.255.255.255"
DEFAULT_PORT = 9
 
 
def create_magic_packet(macaddress):
    if len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, "")
    elif len(macaddress) != 12:
        raise ValueError("Incorrect MAC address format")
 
    return bytes.fromhex("F" * 12 + macaddress * 16)
 
def send_magic_packet(mac, ip_address = BROADCAST_IP, port = DEFAULT_PORT, interface = None):
    packet = create_magic_packet(mac)
 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        if interface is not None:
            sock.bind((interface, 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.connect((ip_address, port))
        sock.send(packet)
 
def main(argv = None):
    parser = argparse.ArgumentParser(
        description="Wake device using the wake on lan protocol.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "mac",
        metavar="mac address",
        help="The mac addresses of the computers you are trying to wake.",
    )
    parser.add_argument(
        "-i",
        metavar="ip",
        default=BROADCAST_IP,
        help="The ip address of the host to send the magic packet to.",
    )
    parser.add_argument(
        "-n",
        metavar="interface",
        default=None,
        help="The ip address of the network adapter to route the magic packet through.",
    )
    args = parser.parse_args(argv)
    send_magic_packet(args.mac, ip_address=args.i, interface=args.n)
 
 
if __name__ == "__main__":
    main()
