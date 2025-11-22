import struct
import sys


def analyze(name):
    try:
        with open(name, 'rb') as file:
            data = file.read(44)
            if len(data) < 44:
                return "NO"
            if data[0:4] != b'RIFF' or data[8:12] != b'WAVE':
                return "NO"
            size = struct.unpack('<I', data[4:8])[0]
            audio_type = struct.unpack('<H', data[20:22])[0]
            channels = struct.unpack('<H', data[22:24])[0]
            rate = struct.unpack('<I', data[24:28])[0]
            bits = struct.unpack('<H', data[34:36])[0]
            data_size = struct.unpack('<I', data[40:44])[0]
            return (f"Size={size}, Type={audio_type}, Channels={channels}, Rate={rate}, Bits={bits}, Data size={data_size}")
    except (FileNotFoundError, IOError, struct.error):
        return "NO"


print(analyze(sys.stdin.readline().strip()))
