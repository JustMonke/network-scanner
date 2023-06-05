import nmap
import time
import ipaddress

# List of IP addresses to monitor
ip_list = ["192.168.18.2", "192.168.18.3", "192.168.18.6", "192.168.18.7", "192.168.18.8", "192.168.18.9",
           "192.168.18.10", "192.168.18.32", "192.168.18.89", "192.168.18.90", "192.168.18.91", "192.168.18.92",
           "192.168.18.93", "192.168.18.94", "192.168.18.97", "192.168.18.98", "192.168.18.99", "192.168.18.111",
           "192.168.18.112", "192.168.18.113", "192.168.18.114", "192.168.18.118", "192.168.18.119", "192.168.18.121",
           "192.168.18.122", "192.168.18.123", "192.168.18.124", "192.168.18.125", "192.168.18.126", "192.168.18.128",
           "192.168.18.131", "192.168.18.138", "192.168.18.182", "192.168.18.206", "192.168.18.207", "192.168.18.222",
           "192.168.18.247"]


previous_ips = []

def network_scan():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.18.0/24', arguments='-sn')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        previous_ips.append(host) 

    #Convert into object for optional sorting
    prv_ip_objects = [ipaddress.ip_address(ip) for ip in previous_ips]
    sorted_prv_ips = sorted(prv_ip_objects)
    sorted_prv_ips_list = [str(ip) for ip in sorted_prv_ips]

    #Convert IP strings to IP objects
    ip_objects1 = set(ipaddress.ip_address(ip) for ip in ip_list)
    ip_objects2 = set(ipaddress.ip_address(ip) for ip in sorted_prv_ips_list)

    #Find the IP addresses added to ip_array1
    added_ips = ip_objects2.difference(ip_objects1)

    #Find the IP addresses removed from ip_array1
    removed_ips = ip_objects1.difference(ip_objects2)

    #Convert IP objects back to strings
    added_ip_list = [str(ip) for ip in added_ips]
    removed_ip_list = [str(ip) for ip in removed_ips]

    #Sort new IP addresses
    added_obj = [ipaddress.ip_address(ip) for ip in added_ip_list]
    sorted_add_ip = sorted(added_obj)
    added_ip_list = [str(ip) for ip in sorted_add_ip]

    #Sort removed IP addresses
    removed_obj = [ipaddress.ip_address(ip) for ip in removed_ip_list]
    sorted_rem_ip = sorted(removed_obj)
    removed_ip_list = [str(ip) for ip in sorted_rem_ip]

    #Print the new IP addresses
    if added_ip_list:
        print("New IP addresses detected: ")
        for ip in added_ip_list:
            print(ip)
    else:
        print("No new IPs are detected")

    print(" ")
    
    #Print the offline IP addresses
    if removed_ip_list:
        print("IP addresses offline: ")
        for ip in removed_ip_list:
            print(ip)
    else:
        print("No IPs are removed")

while(True):
    network_scan()
    print(" ")
    time.sleep(10)
