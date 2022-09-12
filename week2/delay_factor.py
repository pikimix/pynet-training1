from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

host =    {
"host" : "nxos2.lasthop.io",
"username": "pyclass",
"password": getpass(),
"device_type" : "cisco_nxos",
"global_delay_factor": 2,
"fast_cli":False,
}

nc = ConnectHandler(**host)

before = datetime.now()
print(nc.send_command("show lldp neighbors detail"))
after = datetime.now()
before_long = datetime.now()
print(nc.send_command("show lldp neighbors detail", delay_factor=8))
after_long = datetime.now()

print(f"Time sending short delay command: {before.isoformat()}")
print(f"Time after short delay command: {after.isoformat()}")
print(f"Execution short delay time : {after - before}")
print(f"Time sending long delay command: {before.isoformat()}")
print(f"Time after long delay command: {after.isoformat()}")
print(f"Execution long delay time : {after_long - before_long}")

nc.disconnect()
