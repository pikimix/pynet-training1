from netmiko import ConnectHandler
from getpass import getpass

host = {
"host" : "cisco4.lasthop.io",
"username": "pyclass",
"password": getpass(),
"device_type" : "cisco_xe"
}

nc = ConnectHandler(**host)


nc.disconnect()
