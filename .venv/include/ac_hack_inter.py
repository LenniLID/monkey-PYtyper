import customtkinter
from ReadWriteMemory import ReadWriteMemory
import time


dialog = customtkinter.CTkInputDialog(text="Type in a health value:", title="Ac hacks")               #text feld
health_value = dialog.get_input()


rwm = ReadWriteMemory()

process = rwm.get_process_by_name('ac_client.exe')
process.open()

baseaddress_health = 0x400000+0x17E254

health_pointer = process.get_pointer(baseaddress_health, offsets=[0xec])

while True:
    process.write(health_pointer, int(health_value))
    time.sleep(0.5)

