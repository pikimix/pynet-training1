from netmiko import ConnectHandler
from getpass import getpass

host = {
    "host" : "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type" : "cisco_xe"
}

connect = ConnectHandler(**host)
print(connect.find_prompt())
