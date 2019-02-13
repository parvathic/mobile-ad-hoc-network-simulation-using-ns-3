import re

# def trace_parser():
with open("rough", "r") as f:  # Reading the file
    dict = {}
    total_delay = 0
    avg_delay = 0
    tx_counter = 0
    rx_counter = 0
    for line in f:
        if re.search("Payload", line):
            packet_check = re.findall("Tx|Rx", line)  # Checking the packet type

            current_node = int(re.findall("(\/[0-9]+\/)", line)[0].strip("/"))

            time_stamp = float(re.findall("\d+\.\d+", line)[0])  # Checking time stamp

            source_ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)[0]

            destination_ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)[1]

            source_node = int((re.findall("sourceId: [0-9]+", line)[0].split(':')[1]).lstrip())

            destination_node = int((re.findall("destinationId: [0-9]+", line)[0].split(':')[1]).lstrip())

            packet_id = ((re.findall("id [0-9]+", line))[0].split()[1])

            if packet_check == "Tx":
                if current_node != source_node:
                    continue

                tx_counter = tx_counter + 1  # Counter for transmitted packets
                if (source_node, destination_node, id) not in dict:
                    dict[(source_node, destination_node, id)] = time_stamp

            elif packet_check == "Rx":
                if current_node != destination_node:
                    continue

                end_time = time_stamp
                if (source_node, destination_node, id) in dict:
                    start_time = dict[(source_node, destination_node, id)]
                delay = end_time - start_time
                rx_counter = rx_counter + 1
                total_delay = total_delay + delay


            else:
                None

print("Total number of packets transmitted: ", tx_counter)
print("Total number of packets received: ", rx_counter)
if(rx_counter > 0):
    print("Average delay: ", (total_delay / rx_counter))
print("Packet delivery ratio: ", float((rx_counter / tx_counter)))
