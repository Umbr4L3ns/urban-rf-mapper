import binascii

HEX_STREAM = "534f4c45494c5f4e4f49525f52465f424541434f4e5f5631"

def check_header(hex_data):
    raw = binascii.unhexlify(hex_data)
    return raw.decode('ascii', errors='ignore')

if __name__ == "__main__":
    print("[*] Initializing OOK decoder...")
