from netmiko import ConnectHandler


for i in range(1, 4):
    filename = f"router_{i}.txt"
    with open(filename, "w") as file:
        file.write(f"Host of router {i}\n")
        file.write("Username to connect to router\n")
        file.write("Password to connect to router\n")
        file.write("Port of router\n")

print("Router configuration files created: router_1.txt, router_2.txt, router_3.txt")


with open("ospf_routing_protocol.txt", "w") as ospf_file:
    ospf_file.write("router ospf 1\n")
    ospf_file.write("net 0.0.0.0 0.0.0.0 area 0\n")
    ospf_file.write("distance 110\n")
    ospf_file.write("default-information originate\n")

print("OSPF configuration file created: ospf_routing_protocol.txt")

router_details = [
    {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.126.128",
        "username": "sara1",
        "password": "",
        "secret": "cisco1",
        "port": 30003
    },
    {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.126.128",
        "username": "sara2",
        "password": "",
        "secret": "cisco1",
        "port": 30004
    },
    {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.126.128",
        "username": "sara3",
        "password": "",
        "secret": "cisco1",
        "port": 30005
    }
]


with open("ospf_routing_protocol.txt", "r") as ospf_file:
    ospf_commands = ospf_file.readlines()

for router in router_details:
    try:
        connection = ConnectHandler(**router)
        connection.enable()
        connection.send_config_set(ospf_commands)
        print(f"OSPF configuration applied successfully to {router['host']}")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to configure router at {router['host']}: {e}")
