import os
import sys
from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP, UDP


def process_pcap(file_name):
    print('Opening {}...'.format(file_name))

    count = 0
    interesting_packet_count = 0

    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1

        ether_pkt = Ether(pkt_data)
        # if 'type' not in ether_pkt.fields:
        #     # LLC frames will have 'len' instead of 'type'.
        #     # We disregard those
        #     continue
        # # if ether_pkt.src:
        # print(ether_pkt.fields["type"])

        # if ether_pkt.type != 0x0800:
        #     # disregard non-IPv4 packets
        #     continue

        try:
            ip_pkt = ether_pkt[IP]
            print(ip_pkt)
            interesting_packet_count += 1
        except Exception as e:
            print(e)
            continue
        if ip_pkt.proto != 6:
            # Ignore non-TCP packet
            continue

    # interesting_packet_count += 1

    print('{} contains {} packets ({} interesting)'.
          format(file_name, count, interesting_packet_count))


if __name__ == '__main__':
    pcap_file = "all_functions_ish_filtered.pcap"
    if not os.path.isfile(pcap_file):
        print('"{}" does not exist'.format(pcap_file), file=sys.stderr)
        sys.exit(-1)

    process_pcap(pcap_file)
    sys.exit(0)
