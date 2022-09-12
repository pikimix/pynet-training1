from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

host =    {
"host" : "nxos2.lasthop.io",
"username": "pyclass",
"password": getpass(),
"device_type" : "cisco_nxos",
"global_delay_factor": 2,
}

nc = ConnectHandler(**host)

print(f"Time sending command: {datetime.now().isoformat()}")
print(nc.send_command("show lldp neighbors detail"))
print(f"Time after command: {datetime.now().isoformat()}")

nc.disconnect()
