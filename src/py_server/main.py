import pyads
from ctypes import sizeof

#!/usr/bin/python3

ads_net_id = '10.6.105.110.1.1'

plc = pyads.Connection(ads_net_id, pyads.PORT_TC3PLC1)

print("Connecting to TwinCAT PLC..")

plc.open()

print(f"Current connection status:{plc.is_open}")
print(f"Current Status:{plc.read_state()}")

plc.close()
print(f"Current connection status:{plc.is_open}")
