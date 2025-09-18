import scapy.all as scapy
import sys

def scan_network(ip):
    """
    Performs an ARP scan on the specified IP range to find active devices.
    """
    try:
        # Create an ARP request packet
        arp_request = scapy.ARP(pdst=ip)
        
        # Create an Ethernet frame to broadcast the request
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        
        # Combine the packets
        arp_request_broadcast = broadcast/arp_request
        
        # Send the packet and capture the response
        # srp stands for "send and receive packets"
        # timeout=1 sets a 1-second delay for responses
        # verbose=False suppresses unnecessary output
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)
        return clients_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def print_result(results_list):
    """
    Prints the list of found devices in a formatted table.
    """
    if not results_list:
        print("No devices found on the network.")
        return

    print("IP Address\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    # This is a sample IP range. You must change this to your network's range.
    # To find your network's IP range:
    # On Windows: Open Command Prompt and type `ipconfig`. Look for "IPv4 Address" and "Subnet Mask".
    # On macOS/Linux: Open Terminal and type `ifconfig` or `ip a`.
    # A typical range might be "192.168.1.1/24" or "10.0.0.1/24"
    
    # Replace the following line with your actual network IP range
    target_ip_range = "192.168.1.1/24"  
    
    # Run the scan and print the results
    print(f"Scanning network: {target_ip_range}...")
    scan_result = scan_network(target_ip_range)
    
    if scan_result:
        print("\nScan complete. Found the following devices:")
        print_result(scan_result)
    else:
        print("Scan failed. Please ensure scapy and Npcap are installed correctly.")