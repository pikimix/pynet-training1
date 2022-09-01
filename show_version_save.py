from netmiko import ConnectHandler
from getpass import getpass

host ={
    "host" : "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type" : "cisco_xe"
    }

command_output = ""

connect = ConnectHandler(**host)

command_output = connect.send_command("show version")

with open(f"{host['host']}.txt", "w") as file:
    file.write(command_output)
