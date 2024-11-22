from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type="cisco_ios_telnet",
    host="192.168.126.128",
    username="",
    password="",
    secret='cisco1',
    port=30003
)