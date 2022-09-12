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
print(f"Time sending command: {before.isoformat()}")
print(nc.send_command("show lldp neighbors detail"))
after = datetime.now()
print(f"Time after command: {after.isoformat()}")
print(f"Execution time : {(after - before).strftime('%S.%f')}")

nc.disconnect()
