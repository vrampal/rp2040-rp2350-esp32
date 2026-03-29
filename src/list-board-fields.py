import board
import microcontroller
import os

uname = os.uname()
print(f"Machine:  {uname.machine}")
print(f"Nodename: {uname.nodename}")
print(f"Sysname:  {uname.sysname}")
print(f"Release:  {uname.release}")
print(f"Version:  {uname.version}")
cpu = microcontroller.cpu
print(f"CPU Freq: {cpu.frequency}")
print(f"CPU Volt: {cpu.voltage}")
print(f"CPU Temp: {cpu.temperature}")
print(f"Board_id: {board.board_id}")
print("This board offer the following features:")
for feature in dir(board):
    print(feature)