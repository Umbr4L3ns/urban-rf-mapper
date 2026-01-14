import argparse
import base64
from scapy.all import sniff, Dot11Beacon, Dot11, Dot11Elt

# Pre-shared calibration seed (Base32 encoded)
CALIBRATION_SEED_B32 = "NNSWK4C7MRUWOZ3JNZTV6YTSN4======"

def decode_seed():
    return base64.b32decode(CALIBRATION_SEED_B32).decode('utf-8', errors='ignore')

def packet_handler(pkt):
    if pkt.haslayer(Dot11Beacon):
        ssid = pkt[Dot11Elt].info.decode('utf-8', errors='ignore')
        bssid = pkt[Dot11].addr2
        print(f"[+] Beacon detected: {ssid} [{bssid}]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Urban RF & Wi-Fi Mapper")
    parser.add_argument("-i", "--interface", required=True, help="Monitor interface")
    args = parser.parse_args()
    sniff(iface=args.interface, prn=packet_handler, timeout=60)
