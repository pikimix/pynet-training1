from netmiko import ConnectHandler
from getpass import getpass

host = {
"host" : "cisco4.lasthop.io",
"username": "pyclass",
"password": getpass(),
"device_type" : "cisco_xe"
}

nc = ConnectHandler(**host)
output = ""
output += nc.send_command_timing("ping", strip_prompt=False, strip_command=False)
#Protocol [ip]:
output += nc.send_command_timing("", strip_prompt=False, strip_command=False)
#Target IP address:
output += nc.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
#Repeat count [5]:
output += nc.send_command_timing("", strip_prompt=False, strip_command=False)
#Datagram size [100]:
output += nc.send_command_timing("", strip_prompt=False, strip_command=False)
#Timeout in seconds [2]:
output += nc.send_command_timing("", strip_prompt=False, strip_command=False)
#Extended commands [n]:
output += nc.send_command_timing("", strip_prompt=False, strip_command=False)
#Sweep range of sizes [n]:
output += nc.send_command_timing("", strip_prompt=False, strip_command=False)
#Type escape sequence to abort.
#Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
#!!!!!
#Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms
#cisco4#
nc.disconnect()

print(output)
